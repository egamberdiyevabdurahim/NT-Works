from django.contrib import admin

from book.models import CategoryModel, TagModel, BookModel, AuthorModel, CommentModel


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_at', 'updated_at')
    list_display_links = list_display
    search_fields = ('name',)
    list_filter = ('status', 'created_at', 'updated_at')
    ordering = ('name',)


@admin.register(TagModel)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_at', 'updated_at')
    list_display_links = list_display
    search_fields = ('name',)
    list_filter = ('status', 'created_at', 'updated_at')
    ordering = ('name',)


@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'status', 'created_at', 'updated_at')
    list_display_links = list_display
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('status', 'created_at', 'updated_at')
    ordering = ('first_name', 'last_name')


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'category', 'author', 'created_at', 'updated_at')
    list_display_links = list_display
    search_fields = ('title', 'description')
    list_filter = ('status', 'created_at', 'updated_at', 'category', 'author')
    ordering = ('title',)


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'text', 'created_at', 'updated_at')
    list_display_links = list_display
    search_fields = ('book__title', 'user__username', 'text')
    list_filter = ('book__status', 'user__is_staff', 'created_at', 'updated_at')
    ordering = ('-created_at',)
