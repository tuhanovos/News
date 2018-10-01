from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from blog.views import user_add_news, view_one_post, add_comment

urlpatterns = [
    path('add_record', user_add_news, name='add_record'),
    re_path(r'^post/(?P<article_id>\d+)/', view_one_post, name='post'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^post/add_comment/(?P<article_id>[0-9]+)/$', add_comment, name='add_comment'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
