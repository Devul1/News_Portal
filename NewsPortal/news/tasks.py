from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Category, Post
import datetime


@shared_task
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


@shared_task
def weekly_notify():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(time__gte=last_week)
    categories = posts.values_list('categories__title', flat=True)
    subscribers = set(Category.objects.filter(title__in=categories).values_list('subscribers__email', flat=True))

    subject = f'Posts on the last week'
    html_content = render_to_string(
        'weekly_posts.html',
        {'posts': posts}
    )
    
    msg = EmailMultiAlternatives(
        subject, body='', from_email=None, to=subscribers
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
