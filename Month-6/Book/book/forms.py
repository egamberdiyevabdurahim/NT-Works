from django import forms

from book.models import BookModel, TagModel, CategoryModel


class BookForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=CategoryModel.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    tag = forms.ModelMultipleChoiceField(
        queryset=TagModel.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = BookModel
        fields = ['title', 'description', 'photo', 'category', 'tag', 'author']
