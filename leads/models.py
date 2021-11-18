from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# return the defualt user
# User1 = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    agent_user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


class UserProfile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class User(AbstractUser):
    pass


class Agent(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    orgnizatino = models.ForeignKey('UserProfile', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)
