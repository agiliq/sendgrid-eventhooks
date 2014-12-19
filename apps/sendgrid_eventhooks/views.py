from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.dispatch import Signal


sendgrid_email_received = Signal(providing_args=['post_data'] )


def parse_request(data):
    ret=[]
    d={}
    head = data['headers']
    for each in head.split("\n"):
        t=each.split(' ')
        d[t[0][:-1]] = ' '.join(t[1:])
    ret["Subject"] =  data['subject']
    ret["Sender"] =  data['from']
    ret["To"] = data['To']
    ret["Date"] = ['Date']
    ret["Body"] =  data['text']
    return ret


@csrf_exempt
def sendgrid(request):
    if request.method == 'POST':
        post_data = parse_request(request.POST)
        sendgrid_email_received.send(sender=self.__class__, post_data=post_data)
    return render(request, "sendgrid_eventhooks/index.html", {}, )
