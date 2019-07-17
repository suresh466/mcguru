from .forms import QuestionAddForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Info
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def question_add(request):
    template = "questions/add.html"

    form = QuestionAddForm(request.POST or None)
    if Info.objects.filter(identifier=1).exists():
        pass
    else:
        Info.objects.create()

    info = get_object_or_404(Info, identifier=1)

    if form.is_valid():
        question = form.save(commit=False)

        for category in [
                "uncategorized",
                "excel",
                "word",
                "powerpoint",
                "operating_system",
        ]:
            if question.category == category:
                question.question_num = getattr(info, "total_questions_" + category) + 1
                setattr(info, "total_questions_" + category, question.question_num)
        question.question_num = info.total_questions_computer_fundamental + 1
        info.total_questions_computer_fundamental = question.question_num

        info.total_questions += 1

        question.save()
        info.save()
        return redirect("questions:add")

    context = {"title": "add", "form": form, "info": info}

    return render(request, template, context)
