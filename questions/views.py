from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect,get_object_or_404
from .forms import QuestionAddForm
from .models import Info,Question
# Create your views here.

def question_add(request):
    template='questions/add.html'

    form=QuestionAddForm(request.POST or None)

    if form.is_valid():
        question = form.save(commit=False)
        if Info.objects.filter(iteration_num=1).exists():
            pass
        else:
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

def sort():
    for wrong_count in reversed(range(0,16)):
        queryset = Question.objects.filter(wrong_count=wrong_count)
        for query in queryset:
            query.date_created=timezone.now()
            query.save()

def answer(request):
    template='questions/answer.html'
    
    info = get_object_or_404(Info, iteration_num=1)
    
    if info.last_answered == 0:
        question = Question.objects.all().first()

    else:
        last_answered = Question.objects.get(num=info.last_answered)
        try:
            question = last_answered.get_next_by_date_created()
        except ObjectDoesNotExist:
            info = get_object_or_404(Info, iteration_num=1)
            deleted = Question.objects.filter(right_count=2).delete()
            info.total_questions -= deleted[0]
            info.last_answered = 0
            info.save()
            sort()
            return redirect('questions:answer')

    if request.method == 'POST':
        if request.POST['answer'] == question.answer:
            question.right_count += 1
            question.total_right_count += 1
            question.save()
        else:
            question.wrong_count += 1
            question.total_wrong_count += 1
            question.save()
        info.last_answered = question.num
        info.save()
        return redirect('questions:answer')

    context={
            'title':'answer',
            'question': question,
            }

    return render(request,template,context)
