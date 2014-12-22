from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^sendgrid/',
                           include('sendgrid_eventhooks.urls',
                                   namespace="sendgrid")),
                       url(r'^admin/',
                           include(admin.site.urls)), )
