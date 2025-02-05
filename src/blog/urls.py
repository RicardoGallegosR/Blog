from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from posts.views import (index, blog, post, 
        contact, search, post_create,
        post_update, post_delete)
#from .views import *


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', index),
    path('blog/', blog, name='post-list'),
    path('post/<id>/', post, name='post-detail'),
    path('create/', post_create, name='post-create'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete/', post_delete, name='post-delete'),
    path('search/', search, name='search'),
    path('contact/', contact),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)