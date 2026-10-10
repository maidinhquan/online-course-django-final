from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .models import Course, Enrollment, Question, Choice, Submission

def course_list(request):
    courses = Course.objects.all().order_by('name')
    return render(request, 'onlinecourse/course_list_bootstrap.html', {'courses': courses})

def course_details(request, course_id):
    course = get_object_or_404(Course.objects.prefetch_related('lessons', 'questions__choices'), pk=course_id)
    return render(request, 'onlinecourse/course_details_bootstrap.html', {'course': course})

@require_POST
@login_required(login_url='/admin/login/')
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    questions = list(Question.objects.filter(course=course).prefetch_related('choices'))
    if not questions:
        return redirect('onlinecourse:course_details', course_id=course.pk)
    choice_ids = []
    for question in questions:
        value = request.POST.get(f'question_{question.id}')
        if not value or not value.isdigit() or not question.choices.filter(pk=int(value)).exists():
            return render(request, 'onlinecourse/course_details_bootstrap.html', {
                'course': course, 'error': 'Please select one answer for every question.'}, status=400)
        choice_ids.append(int(value))
    with transaction.atomic():
        enrollment, _ = Enrollment.objects.get_or_create(user=request.user, course=course)
        submission = Submission.objects.create(enrollment=enrollment)
        submission.choices.set(Choice.objects.filter(pk__in=choice_ids))
    return redirect('onlinecourse:show_exam_result', course_id=course.pk, submission_id=submission.pk)

@login_required(login_url='/admin/login/')
def show_exam_result(request, course_id, submission_id):
    submission = get_object_or_404(Submission.objects.select_related('enrollment__course','enrollment__user').prefetch_related('choices'),
        pk=submission_id, enrollment__course_id=course_id, enrollment__user=request.user)
    questions = Question.objects.filter(course_id=course_id).prefetch_related('choices')
    selected_ids = set(submission.choices.values_list('id', flat=True))
    rows = []
    earned = possible = 0
    for question in questions:
        correct_ids = {c.id for c in question.choices.all() if c.is_correct}
        selected = {c.id for c in question.choices.all() if c.id in selected_ids}
        is_correct = bool(correct_ids) and selected == correct_ids
        possible += question.grade
        if is_correct: earned += question.grade
        rows.append({'question':question, 'is_correct':is_correct,
                     'selected':', '.join(c.choice_text for c in question.choices.all() if c.id in selected) or 'No answer',
                     'correct':', '.join(c.choice_text for c in question.choices.all() if c.is_correct)})
    score = round(earned * 100 / possible) if possible else 0
    return render(request, 'onlinecourse/exam_result_bootstrap.html', {
        'course': submission.enrollment.course, 'score':score, 'passed':score>=70,
        'earned':earned, 'possible':possible, 'results':rows})
