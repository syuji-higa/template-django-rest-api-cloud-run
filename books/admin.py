from adminsortable.admin import SortableAdmin
from django.contrib import admin

from .models import Book


class BookAdmin(SortableAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")


admin.site.register(Book, BookAdmin)
