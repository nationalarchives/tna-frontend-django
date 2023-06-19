from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def card(request, *args, **kwargs):
    print(request.GET.dict())
    template = loader.get_template("components/card.html")
    params = {
        "supertitle": "Card supertitle",
        "title": "Card title",
        "href": "#",
        "image": {
            "src": "https://loremflickr.com/640/360",
            "alt": "A placeholder image",
        },
        "body": "<p>Card body</p>",
        "actions": [
            {
            "text": "Card action",
            "href": "#",
            "title": "Go and do the action",
            },
        ],
        "htmlElement": "article",
        "classes": "tna-card--demo"
    }
    context = {
        "params": params | request.GET.dict()
    }
    return HttpResponse(template.render(context, request))
