from rest_framework import viewsets

import polls.serializers as serializers
import polls.models as models


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = models.Question.objects.all().order_by("-pub_date")
    serializer_class = serializers.Question
