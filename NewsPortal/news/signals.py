from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import PostCategory


def send_notifications(header, categories, preview, get_absolute_url, subscribers):
    subject = f'New post in the {categories} category'
    
    text_content = (
        f'Post: {header}\n'
        f'Text: {preview}\n\n'
        f'Link to the post: http://127.0.0.1:8000{get_absolute_url}'
    )
    html_content = (
        f'Post: {header}<br>'
        f'Text: {preview}<br><br>'
        f'<a href="http://127.0.0.1:8000{get_absolute_url}">'
        f'Link to the post</a>'
    )

    for email in subscribers:
        msg = EmailMultiAlternatives(subject, text_content, from_email=None, to=[email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()


@receiver(m2m_changed, sender=PostCategory)
def post_created(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.categories.all()
        subscribers: list[str] = []
        
        for category in categories:
            subscribers += category.subscribers.all()
        
        subscribers = [sub.email for sub in subscribers]
        
        send_notifications(instance.header, categories, instance.preview(), instance.get_absolute_url(), subscribers)
