from django.dispatch import Signal


sendgrid_email_received = Signal(providing_args=['data'])
