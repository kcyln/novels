from django.urls import path, re_path
from .views import IndexView, DetailView, ContentView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    re_path(r"^(?P<book_id>\d+)$", DetailView.as_view(), name="detail"),
    re_path(r"^(?P<book_id>\d+)/(?P<num>\d+)$", ContentView.as_view(), name="content"),
]