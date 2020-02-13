from django.contrib import admin
from .models import *
# Register your models here.


class BooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'aurthor', 'created_at', 'publisher')
    list_display_links = ('name', 'category')
    readonly_fields =["views"]

class UserBooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'aurthor', 'created_at', 'status')
    list_display_links = ('name', 'category')
    readonly_fields =["views"]


admin.site.register(Categories)
admin.site.register(AurthorsPro)
admin.site.register(Publishers)
admin.site.register(Books, BooksAdmin)
admin.site.register(UserBooks, UserBooksAdmin)