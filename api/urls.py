from django.urls import path

from api.views import click


urlpatterns = [
    path('click', click),
]