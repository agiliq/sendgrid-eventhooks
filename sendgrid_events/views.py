from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .signals import sendgrid_email_received


def parse_request(data):
    returned_dict = {}
    dict_from_headers = {}
    body = ""
    head = data['headers']
    for each in head.split("\n"):
        row_list = each.split(' ')
        dict_from_headers[row_list[0][:-1]] = ' '.join(row_list[1:])
    returned_dict["subject"] = data['subject']
    returned_dict["sender_name"] = data['from'].split('<')[0].strip()
    returned_dict["sender_email"] = data['from'].split('<')[1][:-1]
    returned_dict["to"] = dict_from_headers['To']
    returned_dict["date"] = dict_from_headers['Date']
    for each in data['text'].split('\n'):
        if each.strip().endswith('> wrote:') or each.strip() == "--":
            break
        else:
            if each.strip():
                body += each
    returned_dict["body"] = body
    return returned_dict


@csrf_exempt
@require_POST
def sendgrid(request):
    if request.method == 'POST':
        post_data = parse_request(request.POST)
        sendgrid_email_received.send(sender=None, data=post_data)
    return HttpResponse()
