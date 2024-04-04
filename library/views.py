from django.shortcuts import render


def library_page(request):
    return render(request, 'librarypage.html')


def library_books_page(request):
    return render(request, 'books.html')