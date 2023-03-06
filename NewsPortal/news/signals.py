from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import Category, PostCategory
from .tasks import send_notifications


@receiver(m2m_changed, sender=PostCategory)
def post_created(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.categories.all()
        subscribers: list[str] = []
        
        for category in categories:
            subscribers += category.subscribers.all()
        
        subscribers = [sub.email for sub in subscribers]
        categories = list(Category.objects.all().values_list('title', flat=True))
        
        send_notifications.delay(instance.header, categories, instance.preview(), instance.get_absolute_url(), subscribers)
