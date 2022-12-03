from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.


class Author(models.Model):
    userAuthor = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(default=0)

    def update_rating(self):
        post_rating = self.post_set.aggregate(ratingSum=Sum('rating')).get('ratingSum')
        if post_rating is None:
            post_rating = 0

        comment_rating = self.userAuthor.comment_set.aggregate(ratingComSum=Sum('rating')).get('ratingComSum')
        if comment_rating is None:
            comment_rating = 0

        compost_rating = 0
        for post in self.post_set.all():
            rating = post.comment_set.aggregate(ratingComSum=Sum('rating')).get('ratingComSum')
            if rating is None:
                rating = 0
            compost_rating += rating

        self.rating = post_rating * 3 + comment_rating + compost_rating
        self.save()


class Category(models.Model):
    title = models.CharField(max_length=64, unique=True)


class Post(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    
    news = 'NW'
    article = 'AR'

    CATEGORY_CHOICES = [
        (news, 'Новость'),
        (article, 'Статья'),
    ]
    
    category_type = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=news)
    time = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', through='PostCategory')
    header = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.header

    def preview(self):
        return f'{self.text[:123]}...'

    def like(self):
        self.rating += 1
        self.save()
    
    def dislike(self):
        self.rating -= 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Comment(models.Model):
    post_com = models.ForeignKey('Post', on_delete=models.CASCADE)
    user_com = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
