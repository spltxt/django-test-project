from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username = 'admin@email.com'
            email = 'admin@email.com'
            password = 'admin'
            admin = User.objects.create_superuser(email=email, username=username, password=password)
            admin.first_name = 'test'
            admin.last_name = 'test'
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
