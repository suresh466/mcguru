from django.contrib import messages
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionAddForm
from .models import Info, Question
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

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


def get_correct_answer(answered_num, question):
    if answered_num == "a" or "1":
        answer = question.opt_a
    elif answered_num == "b" or "2":
        answer = questin.opt_b
    elif answered_num == "c" or "3":
        answer = question.opt_c
    elif answered_num == "d" or "4":
        answer = question.opt_d
    return answer


def answer(request):
    template = "questions/answer.html"

    info = get_object_or_404(Info, identifier=1)
    category = request.path_info.replace("/", "")
    if category == "":
        category = "uncategorized"

    category_last_answered = getattr(info, "last_answered_" + category)

    if category_last_answered == 0:
        try:
            question = Question.objects.get(category=category, question_num=1)
        except Question.DoesNotExist:
            print(
                "===============================++++++++++++++++========================="
            )
            print("Question number 1 does not exist for some reason fix it")
            print(
                "===============================++++++++++++++++========================="
            )
            raise
    else:
        try:
            question = Question.objects.get(
                question_num=category_last_answered + 1, category=category
            )

        except MultipleObjectsReturned:
            print(
                "===============================++++++++++++++++========================="
            )
            print(
                "There is more than one question with question number {} in the {} category fix it.".format(
                    category_last_answered + 1, category
                )
            )
            print(
                "===============================++++++++++++++++========================="
            )
            raise

        except ObjectDoesNotExist:
            messages.success(
                request, "Congratulations all questions are done in this category."
            )
            setattr(info, "last_answered_" + category, 0)
            info.save()
            return redirect("about")

    if request.method == "POST":
        answered_num = request.POST["answer"].lower()
        answer = get_correct_answer(answered_num, question)

        if answer == question.answer:
            question.right_count += 1
            question.total_right_count += 1
            messages.success(
                request,
                "Congratulations, correct answer is {}: {}.".format(
                    answered_num, answer
                ),
            )
        else:
            question.wrong_count += 1
            question.total_wrong_count += 1
            messages.warning(
                request,
                "The correct answer was : {}. but you selected {}. Good luck for this one.".format(
                    answer, answered_num
                ),
            )
        question.save()
        setattr(info, "last_answered_" + category, question.question_num)
        info.save()
        return redirect("home")

    context = {"title": "answer", "question": question, "info": info}

    return render(request, template, context)
