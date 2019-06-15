from django.db import models

# Create your models here.

class Question(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated= models.DateTimeField(auto_now=True)
    num = models.CharField(unique=True,max_length=255,blank=False)
    question = models.TextField(max_length=500,blank=False)
    opt_a = models.CharField(max_length=255,blank=False)
    opt_b = models.CharField(max_length=255,blank=False)
    opt_c = models.CharField(max_length=255,blank=False)
    opt_d = models.CharField(max_length=255,blank=False)
    hint = models.TextField(max_length=500,blank=True)
    answer = models.CharField(max_length=1,blank=False)
    right_count = models.PositiveIntegerField(
            default=0,blank=False,editable=False)
    wrong_count = models.PositiveIntegerField(
            default=0,blank=False,editable=False)
    total_right_count = models.PositiveIntegerField(
            default=0,blank=False,editable=False)
    total_wrong_count = models.PositiveIntegerField(
            default=0,blank=False,editable=False)
