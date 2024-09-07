from django.urls import path, include
from .views import *

urlpatterns = [
path("", Show.as_view(), name = "home"),
path("a/", addTask.as_view(), name = "add-task"),
path("al/", addLayout.as_view(), name = "add-layout"),
path("ac/", addConnector.as_view(), name = "add-connector"),
]