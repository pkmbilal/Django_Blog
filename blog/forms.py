from .models import *
from django import forms
from tinymce.widgets import TinyMCE

class CreateBlog(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE())
    tags_input = forms.CharField(label='Tags', required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter tags separated by commas', 'class': 'block font-poppins w-full p-4 text-lg outline-none border-2 border-gray-100'}))
    class Meta:
        model=Blog
        fields=['title','content','author','tags','is_published']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter blog name', 'class': 'block font-poppins w-full p-4 text-lg outline-none border-2 border-gray-100', 'autofocus':'True'}),
            'tags': forms.SelectMultiple(attrs={'class': 'block font-poppins w-full p-4 text-lg outline-none border-2 border-gray-100'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].empty_label = "Select an author"
        self.fields['author'].widget.attrs.update({'class':'block font-poppins w-full p-4 text-lg outline-none border-2 border-gray-100'})
        self.fields['tags'].empty_label = "Select a tag"

    def save(self, commit=True):
        instance = super().save(commit=False)
        tags_input = self.cleaned_data.get('tags_input')
        if tags_input:
            tags_list = [tag.strip() for tag in tags_input.split(',')]
            # Assuming you have a Tag model
            tags_objects = [Tag.objects.get_or_create(name=tag)[0] for tag in tags_list]
            instance.tags.set(tags_objects)
        if commit:
            instance.save()
        return instance