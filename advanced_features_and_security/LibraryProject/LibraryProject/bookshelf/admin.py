from django.contrib import admin
from .models import Book
from .models import CustomUser, CustomUserAdmin
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')

    list_filter = ('author', 'published_date')

    search_fields = ('title', 'author')
    
admin.site.register(Book)
admin.site.register(CustomUser, CustomUserAdmin)