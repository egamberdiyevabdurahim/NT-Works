from django.contrib import admin

from .models import CategoryModel, BookModel, TagModel, AuthorModel


admin.site.register(CategoryModel)
admin.site.register(BookModel)
admin.site.register(TagModel)
admin.site.register(AuthorModel)
