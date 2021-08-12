from django.core.management import BaseCommand, CommandError
from traitlets.config.loader import ArgumentParser

from customer.models import User


class Command(BaseCommand):
    help = "Activate deactivate users"

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('activate_user', metavar="USER'S PHONE")
        # parser.add_argument('deactivate_user', metavar="USER'S PHONE")

    def handle(self, *args, **options):
        activate_user_phone = options['activate_user']
        # deactivate_user_phone = options['deactivate_user']

        if activate_user_phone:
            try:
                user = User.objects.get(is_superuser=False, phone=activate_user_phone)
                user.is_active = True
                user.save()
                phone = self.style.WARNING(activate_user_phone)
                print(self.style.SUCCESS(f'user with this phone number ({phone}') +
                      self.style.SUCCESS(f') is activate now.'))

            except Exception as e:
                raise CommandError(e)
