from django.shortcuts import render
from django.views.generic import View
from .models import Book, BookContent
# Create your views here.

class IndexView(View):
    def get(self, request):
        return render(request, "index.html")


class DetailView(View):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        content_list = BookContent.objects.filter(book=book).order_by("num")
        totalpage = BookContent.objects.filter(book=book).count()
        last_updated = BookContent.objects.get(book=book, num=totalpage)
        context = {"book": book, "content_list": content_list, "totalpage": totalpage, "last_updated": last_updated}
        return render(request, "detail.html", context)


class ContentView(View):

    def get(self, request, book_id, num):
        # 
        book = Book.objects.get(id=book_id)
        content = BookContent.objects.get(book=book, num=num)
        totalpage = BookContent.objects.filter(book=book).count()
        context = {
            "book": book,
            "content": content,
            "currentpage": num,
            "prevpage": int(num)-1,
            "nextpage": int(num)+1,
            "totalpage": totalpage
        }
        return render(request, "content.html", context, content_type="text/html")