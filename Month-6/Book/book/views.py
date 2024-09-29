from django.shortcuts import render, redirect

from book.models import BookModel, AuthorModel, TagModel, CategoryModel
from book.forms import BookForm


def open_book_view(request, pk):
	book = BookModel.objects.filter(pk=pk).first()

	context = {
		'book': book,
	}
	return render(request, 'open_book.html', context)


def create_book_view(request):
	if request.method == 'POST':
		form = BookForm(request.POST, request.FILES)

		if form.is_valid():
			book = form.save(commit=False)
			book.save()

			book.category.set(form.cleaned_data['category'])
			book.tag.set(form.cleaned_data['tag'])

			return redirect('home')

	authors = AuthorModel.objects.all()
	categories = CategoryModel.objects.all()
	tags = TagModel.objects.all()
	form = BookForm()

	context = {
		'authors': authors,
		'categories': categories,
		'tags': tags,
		'form': form
	}
	return render(request, 'create_book.html', context)


def edit_book_view(request, pk):
	if request.method == 'POST':
		books = BookModel.objects.get(id=pk)
		form = BookForm(request.POST, request.FILES, instance=books)
		if form.is_valid():
			form.save()
			return redirect('home')

	books = BookModel.objects.filter(id=pk).first()
	form = BookForm(instance=books)
	return render(request, 'create_book.html', {'form': form})


def delete_book_view(request, pk):
	book = BookModel.objects.get(id=pk)
	book.delete()
	return redirect('home')
