from django.contrib import admin
from .models import Books, Author, Bookings, Comments
from import_export.admin import ImportExportModelAdmin


@admin.register(Books)
class BookAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "description", "price", "count", "authors")
    list_display_links = ("id", "name", "description", "price", "count", "authors")
    ordering = ("name", )
    search_fields = ("name", "description")
    autocomplete_fields = ("authors",)
    filter = ("id", "name", "description", "price",)


@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ("id", "first_name", "last_name", "birth_date", "email")
    list_display_links = ("id", "first_name", "last_name", "birth_date", "email")
    ordering = ("first_name", "last_name")
    search_fields = ("first_name", )
    filter = ("id", "first_name", "last_name", "birth_date",)


@admin.register(Bookings)
class BookingAdmin(ImportExportModelAdmin):
    list_display = ("id", "get_user_names", "get_book_names", "buy_date", "return_date")
    list_display_links = ("id", "get_user_names", "get_book_names", "buy_date", "return_date")
    ordering = ("buy_date",)
    search_fields = ("get_user_names", "get_book_names", )
    filter = ("id", "get_user_names", "get_book_names",)

    def get_user_names(self, obj):
        return ", ".join([user.username for user in obj.user.all()])
    get_user_names.short_description = "Users"

    def get_book_names(self, obj):
        return ", ".join([book.name for book in obj.book.all()])
    get_book_names.short_description = "Books"


@admin.register(Comments)
class CommentsAdmin(ImportExportModelAdmin):
    list_display = ("id", "comment", "author", "user", "published_date")
    list_display_links = ("id", "comment", "author", "user", "published_date")
    ordering = ("-published_date", )
    search_fields = ("comment", "author", )
    autocomplete_fields = ("author", "user",)
    filter = ("id", "author", "user", "published_date")


