from django.shortcuts import render

# Create your views here.

def question_add(request):
    template='questions/add.html'

    return render(request,template)
