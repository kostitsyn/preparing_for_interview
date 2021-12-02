from django.conf import settings
from django import template

register = template.Library()


@register.filter(name='media_folder_users')
def media_folder_product(string):
    if not string:
        string = 'users_avatars/default.png'

    return f'{settings.MEDIA_URL}{string}'
