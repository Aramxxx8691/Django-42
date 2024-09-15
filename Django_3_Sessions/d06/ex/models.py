from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    reputation = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - Reputation: {self.reputation}"

class Tip(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Tip by {self.author.username} on {self.date.strftime('%Y-%m-%d %H:%M:%S')}"

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tip = models.ForeignKey(Tip, on_delete=models.CASCADE)
    UPVOTE = 'U'
    DOWNVOTE = 'D'
    VOTE_CHOICES = [
        (UPVOTE, 'Upvote'),
        (DOWNVOTE, 'Downvote'),
    ]
    vote_type = models.CharField(max_length=1, choices=VOTE_CHOICES)

    class Meta:
        unique_together = ['user', 'tip']

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
