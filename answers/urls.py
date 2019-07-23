from django.urls import path
from .views import answer
app_name = "answers"

urlpatterns = [
    path("", answer, name="answer"),
    path("uncategorized/", answer, name="uncategorized"),
    path("excel/", answer, name="excel"),
    path("word/", answer, name="word"),
    path("powerpoint/", answer, name="powerpoint"),
    path("operating_system/", answer, name="operating_system"),
    path("computer_misc/", answer, name="computer_misc"),
]
