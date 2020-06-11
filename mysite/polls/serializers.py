from rest_framework import serializers
from polls import models


class Question(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = ["question_text", "pub_date"]
