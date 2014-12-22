[![Build Status](https://api.travis-ci.org/agiliq/sendgrid-eventhooks.svg?branch=develop)](https://travis-ci.org/agiliq/sendgrid-eventhooks)

Django app to receive incoming email notification events from sendgrid
========================================================================

Sendgrid has an incoming event api which will parse incoming emails
and send them to a webhook.

https://sendgrid.com/docs/API_Reference/Webhooks/parse.html

This app provides the webhook to receive this in your Django projects.


Installation
================

    pip install -r sendgrid_eventhooks

Usage
============

* Add sendgrid_events to your `installed_apps`
* Add to urls.py `url("sendgrid", include("sendgrid_events.urls"))`
* Associate the Domain/Hostname and the URL in the Parse API settings page. Parse API settings page is at https://sendgrid.com/developer/reply

Now whenever sendgrid receives the email, it will post to this webhook.

This webwook will consume the data and send a signal called `sendgrid_email_received`. This will have a data attribute with the data received from sendgrid.
