from django.core.management import BaseCommand, CommandError
from traitlets.config.loader import ArgumentParser
from customer.models import User


class Command(BaseCommand):
    """
    This command use for activate deactivate users
    """
    help = "Deactivate activate users"

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('deactivate_user', metavar="USER'S PHONE")

    def handle(self, *args, **options):
        deactivate_user_phone = options['deactivate_user']

        if deactivate_user_phone:
            try:
                user = User.objects.get(is_superuser=False, phone=deactivate_user_phone)
                user.is_active = True
                user.save()
                phone = self.style.WARNING(deactivate_user_phone)
                print(self.style.SUCCESS(f'user with this phone number ({phone}') +
                      self.style.SUCCESS(f') is deactivate now.'))

            except Exception as e:
                raise CommandError(e)
