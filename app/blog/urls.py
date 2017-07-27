from django.conf.urls import url, include
from . import views
from blog import views
from blog import views as profiles_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^blog_list/$', views.blog_list, name='blog_list'),
    url(r'^blog/new/$', views.blog_new, name='blog_new'),
    url(r'^blog/(?P<pk>[0-9]+)/$', views.blog_detail, name='blog_detail'),
    url(r'^blog/(?P<pk>[0-9]+)/edit/$', views.blog_edit, name='blog_edit'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^subscribe/$', views.subscribe, name='subscribe'),
    url(r'^profile/$', profiles_views.userProfile, name='profile'),
    url(r'^$', views.home, name='home'),



]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
