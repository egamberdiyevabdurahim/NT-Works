from django.urls import path

from book.views import open_book_view, create_book_view, edit_book_view, delete_book_view


urlpatterns = [
	path('<int:pk>/', open_book_view, name='open'),
	path('create/', create_book_view, name='create'),
	path('edit/<int:pk>', edit_book_view, name='edit'),
	path('delete/<int:pk>', delete_book_view, name='delete'),
]