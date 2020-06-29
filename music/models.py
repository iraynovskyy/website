from django.db import models
from django.urls import reverse


# Create your models here.
### Red album primary key is 1
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)      # the foreignkey is gonna be 1
                                                                    # if delete album delete all the songs conn to it.
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def get_absolute_url(self):
        # album = models.ForeignKey(Album, on_delete=models.CASCADE)
        # return reverse('music:detail', kwargs={'pk': self.pk})
        return reverse('music:index')
        # album = models.ForeignKey(Album)
        # return reverse('music:detail', kwargs=album.id)

    def __str__(self):
        return self.song_title