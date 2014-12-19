from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    url(r'^', include('sendgrid_eventhooks.urls', namespace="sendgrid")),

    url(r'^admin/', include(admin.site.urls)),
)
