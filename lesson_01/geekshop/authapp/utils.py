from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from urllib.parse import urljoin

def send_verify_mail(user):
    verify_link = reverse('auth:verify', args=[user.email, user.activation_key])
    subject = "Подтверждение учетной записи"
    mail  = f"""
    Подтвердите регистрацию {user.username} на {settings.DOMAIN_NAME}
    Перейдите по ссылке:
    {urljoin(settings.DOMAIN_NAME, verify_link)}
    """
    send_mail(subject, mail, 'noreply@localhost', [user.email,])