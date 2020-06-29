from django.contrib import admin

# Register your models here.
# Wanna be able to create and delete stocks as an admin

from .models import Stock

admin.site.register(Stock)

