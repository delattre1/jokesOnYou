from django.db import models


class Joke(models.Model):
    setup = models.CharField(max_length=300)
    delivery = models.CharField(max_length=300)
