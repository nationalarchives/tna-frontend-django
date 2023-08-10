import json

from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("index.html")
    context = {"button": {"text": "I am a button", "href": "#"}}
    return HttpResponse(template.render(context, request))


def breadcrumbs(request, *args, **kwargs):
    template = loader.get_template("components/breadcrumbs.html")
    params = request.GET.get("params")
    context = {"params": json.loads(params) if params else {}}
    return HttpResponse(template.render(context, request))


def button(request, *args, **kwargs):
    template = loader.get_template("components/button.html")
    params = request.GET.get("params")
    context = {"params": json.loads(params) if params else {}}
    return HttpResponse(template.render(context, request))


def card(request, *args, **kwargs):
    template = loader.get_template("components/card.html")
    params = request.GET.get("params")
    context = {"params": json.loads(params) if params else {}}
    return HttpResponse(template.render(context, request))


def filters(request, *args, **kwargs):
    template = loader.get_template("components/filters.html")
    params = request.GET.get("params")
    context = {"params": json.loads(params) if params else {}}
    return HttpResponse(template.render(context, request))


def footer(request, *args, **kwargs):
    template = loader.get_template("components/footer.html")
    params = request.GET.get("params")
    context = {"params": json.loads(params) if params else {}}
    return HttpResponse(template.render(context, request))


def grid(request, *args, **kwargs):
    template = loader.get_template("components/grid.html")
    params = request.GET.get("params")
    context = {"params": json.loads(params) if params else {}}
    return HttpResponse(template.render(context, request))


def header(request, *args, **kwargs):
    template = loader.get_template("components/header.html")
    params = request.GET.get("params")
    context = {"params": json.loads(params) if params else {}}
    return HttpResponse(template.render(context, request))


def hero(request, *args, **kwargs):
    template = loader.get_template("components/hero.html")
    params = request.GET.get("params")
    context = {"params": json.loads(params) if params else {}}
    return HttpResponse(template.render(context, request))


def indexGrid(request, *args, **kwargs):
    template = loader.get_template("components/index-grid.html")
    params = request.GET.get("params")
    context = {"params": json.loads(params) if params else {}}
    return HttpResponse(template.render(context, request))


def messsage(request, *args, **kwargs):
    template = loader.get_template("components/messsage.html")
    params = request.GET.get("params")
    context = {"params": json.loads(params) if params else {}}
    return HttpResponse(template.render(context, request))


def phaseBanner(request, *args, **kwargs):
    template = loader.get_template("components/phase-banner.html")
    params = request.GET.get("params")
    context = {"params": json.loads(params) if params else {}}
    return HttpResponse(template.render(context, request))


def picture(request, *args, **kwargs):
    template = loader.get_template("components/picture.html")
    params = request.GET.get("params")
    context = {"params": json.loads(params) if params else {}}
    return HttpResponse(template.render(context, request))


def profile(request, *args, **kwargs):
    template = loader.get_template("components/profile.html")
    params = request.GET.get("params")
    context = {"params": json.loads(params) if params else {}}
    return HttpResponse(template.render(context, request))


def sensitiveImage(request, *args, **kwargs):
    template = loader.get_template("components/sensitive-image.html")
    params = request.GET.get("params")
    context = {"params": json.loads(params) if params else {}}
    return HttpResponse(template.render(context, request))


def tabs(request, *args, **kwargs):
    template = loader.get_template("components/tabs.html")
    params = request.GET.get("params")
    context = {"params": json.loads(params) if params else {}}
    return HttpResponse(template.render(context, request))

