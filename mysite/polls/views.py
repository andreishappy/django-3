from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from django.urls import reverse
from polls.models import Question, Choice

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request: HttpRequest) -> HttpResponse:
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request: HttpRequest, *, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/question.html", {"question": question})


def results(request: HttpRequest, *, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request: HttpRequest, *, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    choice_id = request.POST.get("choice")
    if not choice_id:
        return render(
            request,
            "polls/question.html",
            {"question": question, "error_message": "Choice not submitted in form"},
        )
    try:
        selected_choice = question.choice_set.get(pk=choice_id)
    except Choice.DoesNotExist:
        return render(
            request,
            "polls/question.html",
            {"question": question, "error_message": "You didn't select a choice"},
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
