from django.contrib import admin
from myapp.models import quiz

class QuizAdmin(admin.ModelAdmin):
  list_display = [
    'question',
    'option1',
    'option2',
    'option3',
    'option4',
    'correctans',
  ]

admin.site.register(quiz)