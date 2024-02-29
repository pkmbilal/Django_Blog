from .models import *
from django import forms
from tinymce.widgets import TinyMCE

class CreateBlogForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE())
    image = forms.ImageField(required=True)
    class Meta:
        model=Blog
        fields=['title','content','author','tags','image','is_published']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter blog name', 'class': 'block font-poppins w-full p-4 text-lg outline-none border-2 border-gray-100', 'autofocus':'True'}),
            'tags': forms.SelectMultiple(attrs={'class': 'block font-poppins w-full p-4 text-lg outline-none border-2 border-gray-100'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].empty_label = "Select an author"
        self.fields['author'].widget.attrs.update({'class':'block font-poppins w-full p-4 text-lg outline-none border-2 border-gray-100'})