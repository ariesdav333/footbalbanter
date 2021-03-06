"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls  import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.static import serve
from .settings import MEDIA_ROOT
from django.urls import path
from accounts import urls as urls_accounts




urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='posts/')), # This is redirecting to blogposts.html will change this if i want another page to load like login url='posts/'
    url(r'posts/', include('posts.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^accounts/', include(urls_accounts)),
]
