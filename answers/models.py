from django.db import models
import geocoder
import requests
import os

# Create your models here.

class Answers(models.Model):
    user_latitude = models.FloatField(blank=True)
    user_longitude = models.FloatField(blank=True)
    user_answer = models.TextField()

    def answer_return(self, **kwargs):
        g = geocoder.mapbox(self.user_answer, key=os.environ.get("MAPBOX_API_KEY"))
        self.user_latitude = g.latlng[0]
        self.user_longitude = g.latlng[1]
        return super(Answers, self).answer_return(**kwargs)


class Trivia_Questions(models.Model):
    user_answer = models.ForeignKey(Answers, on_delete=models.CASCADE)
    trivia_questions = models.TextField(null=True, blank=True)
    correct_answer = models.TextField()
    correct_longitude = models.FloatField(blank=True)
    correct_latitude = models.FloatField(blank=True)

    def question_generator(self, **kwargs):
        req = requests.get("https://opentdb.com/api.php",params={"amount": 10, "type": "multiple", "category":22})
        req.raise_for_status()
        data = req.json()
        self.trivia_questions = data[""]
        self.correct_answer = data["data"]
        g = geocoder.mapbox(self.correct_answer, key=os.environ.get("MAPBOX_API_KEY"))
        self.correct_longitude=g.latlng[0]
        self.correct_latitude=g.latlng[1]
        return super(Trivia_Questions, self).question_generator(**kwargs)
