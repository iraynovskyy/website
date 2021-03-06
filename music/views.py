from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views import View
from .models import Album
from .forms import UserForm
from django.http import HttpResponseRedirect


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return  render(request, self.template_name, {'form': form})

    # process form data (when user adds some data)
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    # request.user  if you want to get the info about a user. don't write this later.
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})


# JUST DELETE IT IF FAVORITE IN INDEX MAIN MAGE DOESN'T WORK

from django.shortcuts import get_object_or_404
from .models import Song

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "You did not select a valid song",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})

    # else:                                                                 # can be made as a cycle Favorite -> Unfavorite
    #     if selected_song.is_favorite == False:
    #         selected_song.is_favorite = True
    #         selected_song.save()
    #     else:
    #         selected_song.is_favorite = False
    #         selected_song.save()
    #     return render(request, 'music/detail.html', {'album': album})






class SongCreate(CreateView):
    model = Song
    fields = ['album', 'file_type', 'song_title', 'is_favorite']

class SongUpdate(UpdateView):
    model = Song
    fields = ['album', 'file_type', 'song_title', 'is_favorite']

class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('music:index')
