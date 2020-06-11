from django.contrib import admin
from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # This gives sections
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    # If you just want just the fields
    # fields = ["pub_date", "question_text"]

    # Allows for choices to be added in line
    inlines = [ChoiceInline]

    list_display = ("question_text", "pub_date", "was_published_recently")
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
