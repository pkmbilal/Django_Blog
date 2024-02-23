from django.contrib import admin
from .models import Blog, Author, Tag

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'is_published', 'created_on', 'updated_on')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Author)
admin.site.register(Tag)
