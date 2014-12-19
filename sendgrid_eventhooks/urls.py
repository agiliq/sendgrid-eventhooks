from django.conf.urls import patterns, include, url

from . import views


urlpatterns = patterns('',
                       url(r'^email/$', views.email, name="email"),
                       url(r'^$', views.sendgrid, name="webhooks"))
