from django.db import models

# Create your models here.

class Question(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated= models.DateTimeField(auto_now=True)
    num = models.CharField(unique=True,max_length=255)
    question = models.TextField(max_length=500)
    opt_a = models.CharField(max_length=255)
    opt_b = models.CharField(max_length=255)
    opt_c = models.CharField(max_length=255)
    opt_d = models.CharField(max_length=255)
    hint = models.TextField(max_length=500)
    answer = models.CharField(max_length=1)
    right_count = models.PositiveIntegerField()
    wrong_count = models.PositiveIntegerField()
    total_right_count = models.PositiveIntegerField()
    total_wrong_count = models.PositiveIntegerField()
