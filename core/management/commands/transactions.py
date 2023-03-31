from django.core.management.base import BaseCommand
from core.models import Transaction, Category, Currency
from decimal import Decimal
from django.utils import timezone
import random


class Command(BaseCommand):

    def handle(self, *args, **options):
        txs = []
        currencies = list(Currency.objects.all())
        categories = list(Category.objects.all())

        for i in range(1000):
            tx = Transaction(amount=random.randrange(Decimal(1), Decimal(1000)),
                             currency=random.choice(currencies),
                             description="",
                             date=timezone.now() - timezone.timedelta(days=random.randint(1, 365)),
                             category=random.choice(categories)
                             )
            txs.append(tx)

        Transaction.objects.bulk_create(txs)
