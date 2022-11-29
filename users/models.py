from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password


class User(models.Model):
    """
    User model which has username, password and email properties.
    """
    class Meta:
        db_table = 'users'
    username = models.CharField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=100, null=False, unique=True)
    email = models.EmailField(null=False, blank=True)


@receiver(pre_save, sender=User)
def password_hash(sender, instance, *args, **kwargs):
    """
    Converts text password to hash
    :param sender: Model object
    :param instance: current instance will have all the property values
    :param args: args
    :param kwargs: kwargs
    :return:
    """
    instance.password = make_password(instance.password)
