import django.contrib.auth.views as auth_views

from django.conf.urls import patterns, include, url
from django.contrib import admin
from devangelism import views

urlpatterns = patterns(
    '',
    url(r'^accounts/login/$', auth_views.login),
    url(r'^accounts/logout/$', auth_views.logout,
        {'next_page': '/'}),
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home)
)
