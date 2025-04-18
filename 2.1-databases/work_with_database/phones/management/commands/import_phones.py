import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify
from datetime import datetime


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

            for phone in phones:
                phone_object = Phone(id=int(phone[0]),
                                     name=phone[1],
                                     image=phone[2],
                                     price=int(phone[3]),
                                     release_date=datetime.strptime(phone[4],'%Y-%m-%d'),
                                     lte_exists=bool(phone[5]),
                                     slug=slugify(phone[1])
                                     )
                phone_object.save()
