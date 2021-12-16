from django.db import models
import geocoder
import requests

# Create your models here.

class Answers(models.Model):
    user_latitude = models.FloatField(blank=True)
    user_longitude = models.FloatField(blank=True)
    user_answer = models.TextField()

    def answer_return(self, *args, **kwargs):
        g = geocoder.google(self.user_answer, key=GOOGLE_API_KEY)


class Trivia_Questions(models.Model):
    trivia_question = models.TextField()
    correct_answer = models.TextField()
    correct_longitude = models.FloatField(blank=True)
    correct_latitude = models.FloatField(blank=True)
