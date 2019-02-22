from django.conf import settings
from django.urls import reverse
from django.db.models.signals import pre_save, post_save, m2m_changed
from django.db import models

# User import form settings
User = settings.AUTH_USER_MODEL

# Create your models here.
class Contact(models.Model):
    name        = models.CharField(max_length=250, null=True, blank=True)
    email       = models.EmailField(max_length=254, null=True, blank=True)
    content     = models.CharField(max_length=2000, null=True, blank=False)

    def __str__(self):
        return self.email


def pre_save_contact_receiver(sender, instance, *args, **kwargs):
    user = User.objects.all()
    instance.name = 'user short name'
    instance.email = 'user email'
    for x in user:
        instance.name = str(x.short_name)
        instance.email = str(x.email)


pre_save.connect(pre_save_contact_receiver, sender=Contact)
