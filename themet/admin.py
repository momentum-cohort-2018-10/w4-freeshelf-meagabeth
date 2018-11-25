from django.contrib import admin

# Register your models here.
from themet.models import Book


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('title', 'author', 'description',)
    # prepopulated_fields = {'slug': ('title',)}


admin.site.register(Book, BookAdmin)
