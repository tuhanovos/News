"""News URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from blog.views import index, register_user, logout_user, login_user, MyLoginForm

admin.autodiscover()

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index, name='index'),
                  path('registration/', register_user, name='registration'),
                  path('logout/', logout_user, name='logout'),
                  path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('accounts/login/', MyLoginForm.as_view(), name='account_login'),
                  re_path(r'^accounts/', include('allauth.urls')),
                  re_path(r'^comments/', include('django_comments.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]
