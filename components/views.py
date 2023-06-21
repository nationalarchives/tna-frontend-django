import json

from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render({}, request))


def button(request, *args, **kwargs):
    template = loader.get_template("components/button.html")
    params = request.GET.get("params")
    context = json.loads(params) if params else {}
    return HttpResponse(template.render(context, request))


def card(request, *args, **kwargs):
    template = loader.get_template("components/card.html")
    params = request.GET.get("params")
    context = json.loads(params) if params else {}
    return HttpResponse(template.render(context, request))


def footer(request, *args, **kwargs):
    template = loader.get_template("components/footer.html")
    params = request.GET.get("params")
    context = json.loads(params) if params else {}
    return HttpResponse(template.render(context, request))


def grid(request, *args, **kwargs):
    template = loader.get_template("components/grid.html")
    params = request.GET.get("params")
    context = json.loads(params) if params else {}
    return HttpResponse(template.render(context, request))


def sensitiveImage(request, *args, **kwargs):
    template = loader.get_template("components/sensitive-image.html")
    params = request.GET.get("params")
    context = json.loads(params) if params else {}
    return HttpResponse(template.render(context, request))
