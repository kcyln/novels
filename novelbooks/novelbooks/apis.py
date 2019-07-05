from books.models import Book
from django.http import HttpResponse

def get_all_books(*args):
    books = Book.objects.all()
    d = {}
    e = {}
    for book in books:
        
        d["name"] = book.name
        d["author"] = book.author
        
        print(d)

        e.update({"id": book.id, "book": d})

    return HttpResponse(str(e))
    