from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("breadcrumbs", views.breadcrumbs),
    path("button", views.button),
    path("card", views.card),
    path("cookie-banner", views.cookieBanner),
    path("filters", views.filters),
    path("footer", views.footer),
    path("grid", views.grid),
    path("header", views.header),
    path("hero", views.hero),
    path("index-grid", views.indexGrid),
    path("message", views.messsage),
    path("phase-banner", views.phaseBanner),
    path("picture", views.picture),
    path("profile", views.profile),
    path("sensitive-image", views.sensitiveImage),
    path("skip-link", views.skipLink),
    path("tabs", views.tabs),
]
