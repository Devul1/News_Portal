from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import Post


class PostFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='time',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%d',
            attrs={'type': 'date'},
        ),
    )
    
    class Meta:
        model = Post
        fields = {
            'header': ['icontains'],
            'categories': ['exact'],
        }
