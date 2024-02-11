from django.contrib import admin
from .models import PythonQuestions, JSQuestions, HTMLCSSQuestions


# Register your models here.
@admin.register(PythonQuestions)
class PythonQuestionsAdmin(admin.ModelAdmin):
    list_display = ('question_text',)
    search_fields = ('question_text',)


@admin.register(JSQuestions)
class JSQuestionsAdmin(admin.ModelAdmin):
    list_display = ('question_text',)
    search_fields = ('question_text',)


@admin.register(HTMLCSSQuestions)
class HTMLCSSQuestionsAdmin(admin.ModelAdmin):
    list_display = ('question_text',)
    search_fields = ('question_text',)
