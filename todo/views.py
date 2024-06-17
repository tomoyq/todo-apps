from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy

from .models import Todo

# Create your views here.
class IndexViews(generic.ListView):
    model = Todo
    template_name = "todo/index.html"

class RegistViews(generic.CreateView):
    model = Todo
    template_name = "todo/regist.html"
    fields = ["title"]
    success_url = reverse_lazy("todo:index")

class UpdateViews(generic.UpdateView):
    model = Todo
    template_name = "todo/update.html"
    fields = "__all__"
    success_url = reverse_lazy('todo:index')

class DeleteViews(generic.DeleteView):
    model = Todo
    template_name = "todo/delete.html"
    fields = "__all__"
    success_url = reverse_lazy('todo:index')