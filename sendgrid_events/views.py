from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.dispatch import Signal
from django.views.decorators.http import require_POST


sendgrid_email_received = Signal(providing_args=['data'])


def parse_request(data):
    ret = {}
    d = {}
    head = data['headers']
    for each in head.split("\n"):
        t = each.split(' ')
        d[t[0][:-1]] = ' '.join(t[1:])
    ret["Subject"] = data['subject']
    ret["Sender"] = data['from']
    ret["To"] = d['To']
    ret["Date"] = d['Date']
    ret["Body"] = data['text']
    return ret


@csrf_exempt
@require_POST
def sendgrid(request):
    if request.method == 'POST':
        post_data = parse_request(request.POST)
        sendgrid_email_received.send(sender=None, data=post_data)
    return HttpResponse()
