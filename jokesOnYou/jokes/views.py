from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    import requests
    import json
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

    return HttpResponse(f'{setup}... {delivery}')
