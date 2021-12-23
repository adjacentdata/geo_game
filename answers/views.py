from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from answers.models import Answers
# Create your views here.

class AnswersView(CreateView):
    model = Answers
    fields = ['user_latitude', 'user_longitude']
    template_name = 'answers/index.html'
    success_url = '/'

def update_score (request):
    if request.method == 'POST':
        pass
