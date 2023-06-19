from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("button", views.button),
    path("card", views.card),
    path("footer", views.footer),
    path("grid", views.grid),
    path("sensitive-image", views.sensitiveImage),
]
