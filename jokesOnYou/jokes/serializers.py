from rest_framework import serializers
from .models import Joke


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joke
        fields = ['setup', 'delivery']
