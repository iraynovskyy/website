from django.contrib import admin    # pass1234 password
from .models import Album, Song

admin.site.register(Album)
admin.site.register(Song)


# Register your models here.
