from django.contrib import admin
from .models import Blog, Author

# Register your models here.
admin.site.register(Blog)
admin.site.register(Author)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'tags', 'is_published', 'created_on', 'updated_on')