from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from blog.views import user_add_news, view_one_post

urlpatterns = [
    path('add_record', user_add_news, name='add_record'),
    re_path(r'^post/(?P<article_id>\d+)/', view_one_post, name='post'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
