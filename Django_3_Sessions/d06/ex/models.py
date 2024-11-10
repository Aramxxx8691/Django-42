from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    reputation = models.IntegerField(default=0)

    class Meta:
        permissions = [
            ("can_delete_tip", "Can delete tips"),
            ("can_downvote_tip", "Can downvote tips"),
        ]
    
    def __str__(self):
        return self.username


class Tip(models.Model):
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tips')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def __str__(self):
        return f"Tip by {self.author.username}: {self.content[:30]}"

class Vote(models.Model):
    UPVOTE = 'U'
    DOWNVOTE = 'D'
    VOTE_CHOICES = [
        (UPVOTE, 'Upvote'),
        (DOWNVOTE, 'Downvote'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tip = models.ForeignKey(Tip, on_delete=models.CASCADE, related_name='votes')
    vote_type = models.CharField(max_length=1, choices=VOTE_CHOICES)

    def __str__(self):
        return f"{self.user.username} {self.get_vote_type_display()} {self.tip.content[:30]}"
