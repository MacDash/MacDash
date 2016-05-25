from django.core.management.base import BaseCommand, CommandError

from jss import tasks


class Command(BaseCommand):
    help = 'Updates computers from casper'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        tasks.update_computers()

