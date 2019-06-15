from django.shortcuts import render,redirect
from .forms import QuestionAddForm
# Create your views here.

def question_add(request):
    template='questions/add.html'

    form=QuestionAddForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('questions:add')

    context={
            'title':'add',
            'form': form,
            }

    return render(request,template,context)
