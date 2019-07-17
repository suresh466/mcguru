from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.shortcuts import render, redirect, get_object_or_404
from questions.models import Info, Question

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
    category = request.path_info.replace("/", "").replace("answer", "")
    if category == "":
        category = "uncategorized"

    if 'last_answered_' + category not in request.session:
        category_last_answered = request.session['last_answered_' + category] = 0
    else:
        category_last_answered = request.session['last_answered_' + category]

    if category_last_answered == 0:
        try:
            question = Question.objects.get(category=category, question_num=1)
        except Question.DoesNotExist:
            print(
                "=====================++++++++++++++++=================="
            )
            print("Question number 1 does not exist for some reason fix it")
            print(
                "=====================++++++++++++++++=================="
            )
            raise
    else:
        try:
            question = Question.objects.get(
                question_num = category_last_answered + 1, category=category
            )

        except MultipleObjectsReturned:
            print(
                "=====================++++++++++++++++=================="
            )
            print(
                "There is more than one question with question number {} in the {} category fix it.".format(
                    category_last_answered + 1, category
                )
            )
            print(
                "=====================++++++++++++++++=================="
            )
            raise

        except ObjectDoesNotExist:
            messages.success(
                request, "Congratulations all questions are done in this category."
            )
            request.session['last_answered_'+category] = 0
            return redirect("about")

    if request.method == "POST":

        if 'jump' in request.POST:
            jump = int(request.POST["jump"])-1
        else:
            answered_num = request.POST["answer"].lower()
            answer = get_correct_answer(answered_num, question)

            if answer == question.answer:
                messages.success(
                    request,
                    "Congratulations, correct answer is {}: {}.".format(
                        answered_num, answer
                    ),
                )
            else:
                messages.warning(
                    request,
                    "The correct answer was : {}. but you selected {}. Good luck for this one.".format(
                        answer, answered_num
                    ),
                )

        if jump >= 0:
            request.session["last_answered_" + category] = jump
        else:
            request.session["last_answered_" + category] = question.question_num
        return redirect("answers:" + category)
    total_questions = getattr(info, "total_questions_"+category)

    context = {"title": "answer", "question": question, "total_questions": total_questions}

    return render(request, template, context)
