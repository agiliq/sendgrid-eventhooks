from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
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
        sendgrid_email_received.send(sender=None, post_data=post_data)
    return render(request, "sendgrid_eventhooks/index.html", {}, )
