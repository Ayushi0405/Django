from django.contrib import admin
from .models import Question
from django.contrib import admin

from .models import Choice, Question


# ...
admin.site.register(Choice)



class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]


admin.site.register(Question, QuestionAdmin)


class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]


admin.site.register(Question, QuestionAdmin)
# Register your models here.

admin.site.register(Question)
