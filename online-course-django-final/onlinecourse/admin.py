from django.contrib import admin
from .models import Instructor, Learner, Course, Lesson, Question, Choice, Submission, Enrollment

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'course', 'grade')
    list_filter = ('course',)
    inlines = [ChoiceInline]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    inlines = []

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [QuestionInline]

admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Enrollment)
admin.site.register(Submission)
admin.site.register(Choice)
admin.site.site_header = 'OnlineCourse Administration'
