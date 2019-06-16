from django.shortcuts import render,redirect,get_object_or_404
from .forms import QuestionAddForm
from .models import Info
# Create your views here.

def question_add(request):
    template='questions/add.html'

    form=QuestionAddForm(request.POST or None)

    if form.is_valid():
        question = form.save(commit=False)
        if question.num == '1':
            Info.objects.create()

        info = get_object_or_404(Info, iteration_num=1)
        info.total_questions += 1
        info.save()
        question.save()
        return redirect('questions:add')

    context={
            'title':'add',
            'form': form,
            }

    return render(request,template,context)
