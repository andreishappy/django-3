from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from polls.models import Question, Choice
from django.utils import timezone

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/question.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


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
