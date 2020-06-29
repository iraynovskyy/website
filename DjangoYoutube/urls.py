# from django.urls import include, path
# from django.contrib import admin
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('music/', music.site.urls)
#     # path('music/', include('music.urls')),
# ]

from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.urlpatterns import format_suffix_patterns
from companies import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # path('', include('music.urls')),    # if empty space then do...
    url(r'^music/', include('music.urls')),
    url(r'^stocks/', views.StockList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)