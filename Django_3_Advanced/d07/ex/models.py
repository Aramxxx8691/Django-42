from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timesince import timesince

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=64, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    created = models.DateTimeField(auto_now_add=True, null=False)
    updated = models.DateTimeField(auto_now=True, null=False)
    synopsis = models.TextField(max_length=312, null=False)
    content = models.TextField(null=False)

    def __str__(self):
        return self.title

    def time_since_published(self):
        return timesince(self.created, timezone.now())

class UserFavouriteArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'article'], name='unique_favorite')
        ]

    def __str__(self):
        return self.article.title
