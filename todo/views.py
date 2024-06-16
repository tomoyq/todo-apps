from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic

from .models import Todo

# Create your views here.
class IndexViews(generic.ListView):
    template_name = "todo/index.html"
    model = Todo