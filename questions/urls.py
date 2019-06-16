from django.urls import path
from .views import question_add,answer

app_name='questions'
urlpatterns = [
    path('add/', question_add, name='add'),
    path('answer/', answer, name='answer'),
]
