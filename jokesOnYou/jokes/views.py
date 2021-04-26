import concurrent.futures
from django.shortcuts import render
from threading import Thread
from django.http import HttpResponse
from urllib.parse import quote, unquote
import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Joke
from .serializers import JokeSerializer


def getJoke():
    # https://rapidapi.com/translated/api/mymemory-translation-memory/endpoints - Translate API
    url = "https://jokeapi-v2.p.rapidapi.com/joke/Any"

    querystring = {"idRange": "0-300",
                   "format": "json", "type": "twopart"}

    headers = {
        'x-rapidapi-key': "89c0a9ae30msh9ce4247e0c650ffp11acb3jsnd84b2181f708",
        'x-rapidapi-host': "jokeapi-v2.p.rapidapi.com"
    }

    response = requests.get(
        url, headers=headers, params=querystring).json()

    setup = response['setup']
    delivery = response['delivery']

    return setup, delivery


def translateJoke(joke):
    url = "https://translated-mymemory---translation-memory.p.rapidapi.com/api/get"
    querystring = {"q": joke, "langpair": "en|pt",
                   "onlyprivate": "0", "mt": "1"}

    headers = {
        'x-rapidapi-key': "89c0a9ae30msh9ce4247e0c650ffp11acb3jsnd84b2181f708",
        'x-rapidapi-host': "translated-mymemory---translation-memory.p.rapidapi.com"
    }

    response = requests.get(
        url, headers=headers, params=querystring).json()

    return response['responseData']['translatedText']


def index(request):
    setup, delivery = getJoke()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        setup_pt = executor.submit(translateJoke, setup).result()
        delivery_pt = executor.submit(translateJoke, delivery).result()

    return render(request, 'jokes/index.html', {'setup': setup_pt, 'delivery': delivery_pt})


@api_view(['GET', 'POST'])
def api_joke(request):

    setup, delivery = getJoke()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        setup_pt = executor.submit(translateJoke, setup).result()
        delivery_pt = executor.submit(translateJoke, delivery).result()

    joke = Joke(setup=setup_pt, delivery=delivery_pt)
    serialized_joke = JokeSerializer(joke)

    return Response(serialized_joke.data)
