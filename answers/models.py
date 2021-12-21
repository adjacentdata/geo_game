from types import coroutine
from django.db import models
import geocoder
import requests
import os
import random

questions = [
    {
      "category": "Geography",
      "type": "multiple",
      "difficulty": "medium",
      "question": "In which English county is Stonehenge?",
      "correct_answer": "Wiltshire",
      "lat": 51.78469720037877,
      "long": -1.636201416641436
    },
    {
      "category": "Geography",
      "type": "multiple",
      "difficulty": "medium",
      "question": "Where is the towns/villages in the Pacific Island nation of Kiribati:",
      "correct_answer": "",
      "lat":-1.603342440877318,
      "long":-168.5840222586849
    },
    {
      "category": "Geography",
      "type": "multiple",
      "difficulty": "easy",
      "question": "What state has the nickname The First State",
      "correct_answer": "The First State",
      "lat":38.96047816076582,
      "long": -75.52410151111027
    },
    {
      "category": "Geography",
      "type": "multiple",
      "difficulty": "easy",
      "question": "What is the name of the peninsula containing Spain and Portugal?",
      "correct_answer": "Iberian Peninsula",
      "lat": 40.61650098153299,
      "long": -4.098477881100619
    },
    {
      "category": "Geography",
      "type": "multiple",
      "difficulty": "medium",
      "question": "Where is the Anatolia land mass located today?",
      "correct_answer": "Anatolia",
      "lat": 39.240174900626556,
      "long": 35.258973853210975
    },
    {
      "category": "Geography",
      "type": "multiple",
      "difficulty": "hard",
      "question": "What is the largest freshwater lake by volume?",
      "correct_answer": "Lake Baikal",
      "lat": 53.63319057234089,
      "long": 108.16869877422177
    }
]

class Answers(models.Model):
    user_answer = models.TextField()
    user_latitude = models.FloatField(blank=True, null=True)
    user_longitude = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.user_answer, key=os.environ.get("MAPBOX_API_KEY"))
        coordinates = g.latlng
        self.user_latitude = coordinates[0]
        self.user_longitude = coordinates[1]
        return super(Answers, self).save(*args,**kwargs)


class Trivia_Questions(models.Model):
    trivia_questions = models.TextField(null=True, blank=True)
    correct_answer = models.TextField(null=True, blank=True)
    correct_longitude = models.FloatField(blank=True, null=True)
    correct_latitude = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # req = requests.get("https://opentdb.com/api.php",params={"amount": 10, "type": "multiple", "category":22})
        # req.raise_for_status()
        # data = req.json()
        chosen_question = questions[random.randint(0, len(questions)-1)]
        self.trivia_questions = chosen_question["question"]
        self.correct_answer = chosen_question["correct_answer"]
        self.correct_longitude= chosen_question['lat']
        self.correct_latitude= chosen_question['long']
        return super(Trivia_Questions, self).save(*args, **kwargs)
