from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    price = models.IntegerField()
    RATING = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'),)

    rating = models.IntegerField(choices=RATING, default=1,)
    # image uproad
    img = models.FileField(null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
