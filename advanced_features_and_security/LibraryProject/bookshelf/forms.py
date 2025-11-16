# bookshelf/forms.py
from django import forms
from .models import Book  # assuming you have a Book model

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=200, required=False)

    def clean_query(self):
        q = self.cleaned_data.get("query", "")
        # Additional sanitation if needed (strip whitespace)
        return q.strip()

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "description", "published_date"]  # adjust to your model fields

    # Example custom validation
    def clean_title(self):
        title = self.cleaned_data.get("title", "")
        if "<script" in title.lower():
            raise forms.ValidationError("Invalid characters in title.")
        return title.strip()
