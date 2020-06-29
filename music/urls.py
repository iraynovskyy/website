# create urls just for this music section
#
from django.conf.urls import url
# from django.urls import path, url
from . import views                         # import from this folder

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /music/712/
    # /music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album=2/update
    url(r'album=(?P<pk>[0-9]+)/update$', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    # # /music/<album>/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

    # /music/album/<album>/song/add/
    url(r'album/(?P<pk>[0-9]+)/song/add$', views.SongCreate.as_view(), name='song-add'),

    # /music/album/<album>/song/2/update
    url(r'album/(?P<pk>[0-9]+)/update/$', views.SongUpdate.as_view(), name='song-update'),

    # /music/album/song/2/delete/
    url(r'album/song/(?P<pk>[0-9]+)/delete/$', views.SongDelete.as_view(), name='song-delete'),
]