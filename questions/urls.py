from django.urls import path
from .views import question_add

app_name='questions'
urlpatterns = [
    path('add/', question_add, name='add')
]
