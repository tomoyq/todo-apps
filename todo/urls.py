from django.urls import path

from . import views

app_name = "todo"
urlpatterns = [
    path("", views.IndexViews.as_view(), name = "index"),
    path("test/", views.RegistViews.as_view(), name = "regist"),
    path("update/<int:pk>/", views.UpdateViews.as_view(), name = "reload")
]