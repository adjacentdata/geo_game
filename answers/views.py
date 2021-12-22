from django.shortcuts import render
from django.views.generic.edit import CreateView
from answers.models import Answers
# Create your views here.

class AnswersView(CreateView):
    model = Answers
    fields = ['user_latitude', 'user_longitude']
    template_name = 'answers/index.html'
    success_url = '/'
