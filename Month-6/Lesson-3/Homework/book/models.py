from django.db import models
from django.contrib.auth.models import User


class CreatedAts(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.created_at}/{self.updated_at}"


class CategoryModel(CreatedAts, models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class TagModel(CreatedAts, models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name


class AuthorModel(CreatedAts, models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BookModel(CreatedAts, models.Model):
    STATUS = (
        ("Published", "Published"),
        ("Unpublished", "Unpublished"),
        ("Deleted", "Deleted"),
        ("Pending", "Pending"),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=64, choices=STATUS, default="Pending")
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(TagModel)
    author = models.ForeignKey(AuthorModel, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title


class CommentModel(CreatedAts, models.Model):
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"{self.user}/{self.book}"
