from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    print('=========sender========', sender)
    print('=========instance========', instance)
    print('=========created========', created)
    '''
    instance is object called to this function
    sender is User Created
    created: boolean, True if created, False if not
    '''
    if created:
        Profile.objects.create(user=instance) # create Profile instance for each new User
