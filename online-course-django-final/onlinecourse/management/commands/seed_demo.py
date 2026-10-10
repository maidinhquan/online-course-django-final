from django.core.management.base import BaseCommand
from onlinecourse.models import Course, Lesson, Question, Choice
class Command(BaseCommand):
    help = 'Create a demonstration course and exam'
    def handle(self, *args, **options):
        course,_=Course.objects.get_or_create(name='Introduction to Python', defaults={'description':'Learn Python fundamentals and assess your knowledge.'})
        for i,(title,content) in enumerate([('Variables','Store values using names.'),('Conditions','Use if statements for branching.'),('Functions','Write reusable code with def.')],1):
            Lesson.objects.get_or_create(course=course,title=title,defaults={'content':content,'order':i})
        sample=[('Which keyword creates a function?', [('def',True),('func',False),('function',False)]),('What type is 42?', [('int',True),('str',False),('bool',False)]),('Which operator tests equality?', [('==',True),('=',False),('!=',False)])]
        for text,choices in sample:
            q,_=Question.objects.get_or_create(course=course,question_text=text,defaults={'grade':10})
            for label,correct in choices: Choice.objects.get_or_create(question=q,choice_text=label,defaults={'is_correct':correct})
        self.stdout.write(self.style.SUCCESS(f'Demo ready: /course/{course.id}/'))
