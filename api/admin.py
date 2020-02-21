from django.contrib import admin
from .models import Book, BookNumber, Character, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'published', 'is_published', 'cover')
    list_filter = ('published', 'is_published')
    list_search = ('title', 'description')
    list_editable = ('is_published',)


admin.site.register(BookNumber)
admin.site.register(Character)
admin.site.register(Author)
