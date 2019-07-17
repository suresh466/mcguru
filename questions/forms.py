from django import forms
from .models import Question


class QuestionAddForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"
