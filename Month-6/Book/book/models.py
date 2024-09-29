from django.db import models


class UsefulModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class CategoryModel(models.Model):
	name = models.CharField(max_length=64)

	def __str__(self):
		return self.name


class TagModel(models.Model):
	name = models.CharField(max_length=64)

	def __str__(self):
		return self.name


class AuthorModel(UsefulModel, models.Model):
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	description = models.TextField()
	photo = models.ImageField(upload_to='author_photo/')

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

	@property
	def full_name(self):
		return f'{self.first_name} {self.last_name}'


class BookModel(UsefulModel, models.Model):
	title = models.CharField(max_length=264)
	description = models.TextField()
	photo = models.ImageField(upload_to='books_photo/')
	category = models.ManyToManyField(CategoryModel)
	tag = models.ManyToManyField(TagModel)
	author = models.ForeignKey(AuthorModel, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.title
