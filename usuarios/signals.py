# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Persona

@receiver(post_save, sender=Persona)
def create_user_for_persona(sender, instance, created, **kwargs):
    if created and not instance.user:
        username = instance.identificacion
        password = instance.identificacion #User.objects.make_random_password()
        user = User.objects.create_user(
            username=username,
            email=instance.email,
            password=password,
            first_name=instance.nombres,
            last_name=instance.apellidos
        )
        instance.user = user
        instance.save()
