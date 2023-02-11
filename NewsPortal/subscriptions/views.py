from django.contrib.auth.decorators import login_required
from django.db.models import Exists, OuterRef
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from news.models import Category

# Create your views here.


@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            user = request.user
            category.subscribers.add(user)
        elif action == 'unsubscribe':
            user=request.user
            category.subscribers.remove(user.id)

    categories = Category.objects.annotate(
        is_subscriber = Exists(
            request.user.categories.filter(
                pk=OuterRef('pk'),
            )
        )
    ).order_by('title')

    return render(
        request,
        'subscriptions.html',
        {'categories': categories},
    )
