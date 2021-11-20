import os
import json
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    def handle(self, *args, **options):
        file_path = os.path.join(settings.BASE_DIR, 'secret.json')
        if os.path.exists(file_path):
            with open(os.path.join(settings.BASE_DIR, 'secret.json')) as f:
                data = json.load(f)
            user = get_user_model()
            try:
                user.objects.create_superuser(
                    username=data['SU_USERNAME'],
                    email=data['SU_EMAIL'],
                    password=data['SU_PASSWORD']
                )
            except Exception:
                raise CommandError('Не удалось создать суперпользователя')
            else:
                self.stdout.write(self.style.SUCCESS("Суперпользователь успешно создан!"))
        else:
            raise CommandError('Файл secret.json не найден')
