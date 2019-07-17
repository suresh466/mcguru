from .forms import QuestionAddForm
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

        if question.category == "Uncategorized":
            question.question_num = info.total_questions_uncategorized + 1
            info.total_questions_uncategorized = question.question_num

        elif question.category == "Excel":
            question.question_num = info.total_questions_excel + 1
            info.total_questions_excel = question.question_num

        elif question.category == "Word":
            question.question_num = info.total_questions_word + 1
            info.total_questions_word = question.question_num

        elif question.category == "Powerpoint":
            question.question_num = info.total_questions_powerpoint + 1
            info.total_questions_powerpoint = question.question_num

        elif question.category == "Operating System":
            question.question_num = info.total_questions_operating_system + 1
            info.total_questions_operating_system = question.question_num

        else:
            question.question_num = info.total_questions_computer_fundamental + 1
            info.total_questions_computer_fundamental = question.question_num

        info.total_questions += 1

        question.save()
        info.save()
        return redirect("add")

    context = {"title": "add", "form": form, "info": info}

    return render(request, template, context)
