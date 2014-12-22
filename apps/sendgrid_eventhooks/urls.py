from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
                       url(r'^email/$', views.email, name="email"),
                       url(r'^$', views.sendgrid, name="webhooks"))
