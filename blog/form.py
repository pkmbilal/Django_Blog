from .models import *
from django import forms


class CreateBlog(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','content','author','tags','is_published']