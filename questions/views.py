from django.shortcuts import render,redirect,get_object_or_404
from .forms import QuestionAddForm
from .models import Info,Question
# Create your views here.

def question_add(request):
    template='questions/add.html'

    form=QuestionAddForm(request.POST or None)

    if form.is_valid():
        question = form.save(commit=False)
        if question.num == 1:
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

def answer(request):
    template='questions/answer.html'
    
    info = get_object_or_404(Info, iteration_num=1)
    if info.last_answered == info.total_questions:
        Question.objects.filter(right_count=2).delete()
        question = 'False'
    else:
        question = get_object_or_404(Question, num=info.last_answered+1)

    if request.method == 'POST':
        if request.POST['answer'] == question.answer:
            question.right_count += 1
            question.total_right_count += 1
            question.save()
            print('you are correct')
        else:
            question.wrong_count += 1
            question.total_wrong_count += 1
            question.save()
            print('you are wrong')
        info.last_answered = question.num
        info.save()
        return redirect('questions:answer')

    context={
            'title':'answer',
            'question': question,
            }

    return render(request,template,context)
