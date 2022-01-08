from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from answers.models import Trivia_Questions
import random
# Create your views here.


def question(request):
    random_int = random.randint(0, 1)
    context = Trivia_Questions.objects.values()[random_int]
    return render(request, 'answers/index.html', {"context" : context})

def update_score (request):
    if request.method == 'POST':
        pass
