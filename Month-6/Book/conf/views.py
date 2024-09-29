from django.shortcuts import render

from book.models import BookModel


def home_view(request):
	books = BookModel.objects.all()
	return render(request, 'home.html', {'books': books})
