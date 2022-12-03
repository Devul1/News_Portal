from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime

# Create your views here.

class PostList(ListView):
    model = Post
    ordering = 'header'
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow
        context['sorted_posts'] = Post.objects.all().order_by('-time')
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'