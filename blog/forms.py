from .models import *
from django import forms


class CreateBlog(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','content','author','tags','is_published']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter blog name', 'class': 'block font-poppins w-full p-4 text-lg outline-none border-2 border-gray-100', 'autofocus':'True'}),
            'content': forms.Textarea(attrs={'placeholder': 'Enter blog content', 'class': 'block font-poppins w-full p-4 text-lg outline-none border-2 border-gray-100'}),
            'tags': forms.TextInput(attrs={'placeholder': 'Enter tag name', 'class': 'block font-poppins w-full p-4 text-lg outline-none border-2 border-gray-100'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].empty_label = "Select an author"
        self.fields['author'].widget.attrs.update({'class':'block font-poppins w-full p-4 text-lg outline-none border-2 border-gray-100'})