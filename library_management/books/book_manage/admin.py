from django.contrib import admin
from .models import books_manage,patron_manage,book_borrow

# Register your models here.


admin.site.register(books_manage)
admin.site.register(patron_manage)
admin.site.register(book_borrow)
