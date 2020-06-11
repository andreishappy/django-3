from django.urls import path, include
from polls import views
from polls import api
from rest_framework import routers

app_name = "polls"

router = routers.DefaultRouter()
router.register(r"questions", api.QuestionViewSet)

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("api/", include(router.urls)),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
