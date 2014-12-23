import logging

from django.dispatch import receiver

from sendgrid_events.signals import sendgrid_email_received


logger = logging.getLogger()
logger.setLevel(logging.INFO)


@receiver(sendgrid_email_received)
def sendgrid_email_received_callback(sender, **kwargs):
    data = kwargs['data']
    logging.info(data['Sender'])
    logging.info(data['Subject'])
    logging.info(data['Body'])
