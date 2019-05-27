from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class IndexView(View):
    def get(self, request):
        return render(request, "index.html")


class DetailView(View):
    # def get(self, request, book_id, content_id):
    def get(self, request):
    
        return render(request, "detail.html")


class ContentView(View):
    # def get(self, request, book_id, content_id):
    def get(self, request):
    
        return render(request, "content.html")