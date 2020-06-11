from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404
from polls.models import Question

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request: HttpRequest) -> HttpResponse:
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request: HttpRequest, *, question_id: int) -> HttpResponse:
    question: Question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/question.html", {"question": question})


def results(request: HttpRequest, *, question_id: int) -> HttpResponse:
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request: HttpRequest, *, question_id: int) -> HttpResponse:
    return HttpResponse("You're voting on question %s." % question_id)
