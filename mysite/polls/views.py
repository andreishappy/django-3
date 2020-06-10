from django.shortcuts import render
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
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404(f"Question with id {question_id} does not exist")
    return render(request, "polls/question.html", {"question": question})


def results(request: HttpRequest, *, question_id: int) -> HttpResponse:
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request: HttpRequest, *, question_id: int) -> HttpResponse:
    return HttpResponse("You're voting on question %s." % question_id)
