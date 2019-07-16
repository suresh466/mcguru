from django.db import models

# Create your models here.

UN = 'uncategorized'
XLS = 'excel'
DOC = 'word'
PPT = 'powerpoint'
OS = 'operating-system'
MISC = 'computer-misc'

CATEGORIES_CHOICE = (
        (UN, 'Uncategorized'),
        (XLS, 'Excel'),
        (DOC,'Word'),
        (PPT,'Powerpoint'),
        (OS,'Operating System'),
        (MISC,'Computer Fundamental'),
        )

class Question(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated= models.DateTimeField(auto_now=True)
    question_num = models.PositiveIntegerField(editable=False)
    question = models.TextField(max_length=500,blank=False)
    opt_a = models.CharField(max_length=255,blank=False)
    opt_b = models.CharField(max_length=255,blank=False)
    opt_c = models.CharField(max_length=255,blank=False)
    opt_d = models.CharField(max_length=255,blank=False)
    answer = models.CharField(max_length=1,blank=False)
    category = models.CharField(choices=CATEGORIES_CHOICE,default='Uncategorized', max_length=20)
    #hint = models.CharField(max_length=500,blank=True)
    right_count = models.PositiveIntegerField(
            default=0,blank=False,editable=False)
    wrong_count = models.PositiveIntegerField(
            default=0,blank=False,editable=False)
    total_right_count = models.PositiveIntegerField(
            default=0,blank=False,editable=False)
    total_wrong_count = models.PositiveIntegerField(
            default=0,blank=False,editable=False)

    def __str__(self):
        return str(self.question_num)

class Info(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    total_questions = models.PositiveIntegerField(blank=False,default=0)
    total_questions_uncategorized = models.PositiveIntegerField(blank=False,default=0)
    total_questions_excel = models.PositiveIntegerField(blank=False,default=0)
    total_questions_word = models.PositiveIntegerField(blank=False,default=0)
    total_questions_powerpoint = models.PositiveIntegerField(blank=False,default=0)
    total_questions_operating_system = models.PositiveIntegerField(blank=False,default=0)
    total_questions_computer_fundamental = models.PositiveIntegerField(blank=False,default=0)
    last_answered = models.PositiveIntegerField(blank=False,default=0)
    last_answered_uncategorized = models.PositiveIntegerField(blank=False,default=0)
    last_answered_excel = models.PositiveIntegerField(blank=False,default=0)
    last_answered_word = models.PositiveIntegerField(blank=False,default=0)
    last_answered_powerpoint = models.PositiveIntegerField(blank=False,default=0)
    last_answered_operating_system = models.PositiveIntegerField(blank=False,default=0)
    last_answered_computer_fundamental = models.PositiveIntegerField(blank=False,default=0)
    identifier = models.PositiveIntegerField(default=1,blank=False,editable=False)

    def __str__(self):
        return str(self.total_questions)
