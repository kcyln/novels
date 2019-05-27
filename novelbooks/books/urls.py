from django.urls import path, re_path
from .views import IndexView, DetailView, ContentView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    # re_path(r"(<?Pbook_id>.*?)/(<?Pcontent_id>\d+)", DetailView.as_view(), name="detail")
    path("123", DetailView.as_view(), name="detail"),
    path("456", ContentView.as_view(), name="content"),
]