import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return HttpResponse("Hello, world!")

def button(request, *args, **kwargs):
    template = loader.get_template("components/button.html")
    params = request.GET.get('params')
    context = {
        "params": json.loads(params) if params else {}
    }
    return HttpResponse(template.render(context, request))

def card(request, *args, **kwargs):
    template = loader.get_template("components/card.html")
    # params = {
    #     "supertitle": "Card supertitle",
    #     "title": "Card title",
    #     "href": "#",
    #     "image": {
    #         "src": "https://loremflickr.com/640/360",
    #         "alt": "A placeholder image",
    #     },
    #     "body": "<p>Card body</p>",
    #     "actions": [
    #         {
    #         "text": "Card action",
    #         "href": "#",
    #         "title": "Go and do the action",
    #         },
    #     ],
    #     "htmlElement": "article",
    #     "classes": "tna-card--demo"
    # }
    params = request.GET.get('params')
    context = {
        "params": json.loads(params) if params else {}
    }
    return HttpResponse(template.render(context, request))

def footer(request, *args, **kwargs):
    template = loader.get_template("components/footer.html")
    params = request.GET.get('params')
    context = {
        "params": json.loads(params) if params else {}
    }
    return HttpResponse(template.render(context, request))

def grid(request, *args, **kwargs):
    template = loader.get_template("components/grid.html")
    params = request.GET.get('params')
    context = {
        "params": json.loads(params) if params else {}
    }
    return HttpResponse(template.render(context, request))

def sensitiveImage(request, *args, **kwargs):
    template = loader.get_template("components/sensitive-image.html")
    params = request.GET.get('params')
    context = {
        "params": json.loads(params) if params else {}
    }
    return HttpResponse(template.render(context, request))
