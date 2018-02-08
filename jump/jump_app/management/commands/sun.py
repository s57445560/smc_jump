#!/usr/bin/python

from django.core.management.base import BaseCommand, CommandError
from jump_app.models import UserInfo
 
class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
    #必须实现的方法 
    def handle(self, *args, **options):
        try:
            poll = UserInfo.objects.filter(user='sunyang')
        except :
            raise CommandError('Poll does not exist')
 
        print(poll) 
        self.stdout.write('Successfully closed poll %s' % poll[0].passwd)
