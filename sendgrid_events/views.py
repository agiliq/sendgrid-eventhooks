from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .signals import sendgrid_email_received


def parse_request(data):
    returned_dict = {}
    dict_from_headers = {}
    head = data['headers']
    for each in head.split("\n"):
        row_list = each.split(' ')
        dict_from_headers[row_list[0][:-1]] = ' '.join(row_list[1:])
    returned_dict["Subject"] = data['subject']
    returned_dict["Sender"] = data['from']
    returned_dict["To"] = dict_from_headers['To']
    returned_dict["Date"] = dict_from_headers['Date']
    returned_dict["Body"] = data.get('text', '')
    return returned_dict


@csrf_exempt
@require_POST
def sendgrid(request):
    if request.method == 'POST':
        post_data = parse_request(request.POST)
        sendgrid_email_received.send(sender=None, data=post_data)
    return HttpResponse()
