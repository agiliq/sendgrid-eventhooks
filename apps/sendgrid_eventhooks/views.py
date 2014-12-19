from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail


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
def email(request):
    resp = send_mail('Subject',
                     'Tell us what you have accomplished today.',
                     'hello@worksummarizer.agiliq.com',
                     ['youremail@something.com'], # to list needs to be filled
                     fail_silently=False)
    return HttpResponseRedirect(reverse('sendgrid:webhooks'))

@csrf_exempt
def sendgrid(request):
    if request.method == 'POST':
        body = parse_request(request.POST)
        resp = send_mail("SendGrid Response", body,
                         'hello@worksummarizer.agiliq.com',
                         ['youremail@something.com'], # To list needs to me filled
                         fail_silently=False)

    return render(request, "sendgrid_eventhooks/index.html", {}, )
