from django.core.management.base import BaseCommand, CommandError

from optparse import make_option

import random
import logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    args = 'create, delete, info'
    help = 'Multidb management'

    option_list = BaseCommand.option_list + (
#        make_option('--delete', action='store_true', dest='delete', default=False, help='Delete poll instead of closing it'),
    )
        
    def handle(self, subcommand, **kwargs):
        pass
