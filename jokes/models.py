from django.db import models


class Joke(models.Model):
    setup = models.CharField(max_length=300)
    delivery = models.CharField(max_length=300)
    joke_id = models.IntegerField()

    def __str__(self):
        return f'{self.id}, {self.setup}'
