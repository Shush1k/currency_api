import datetime
from dataclasses import dataclass

from django.contrib.auth.models import User
from django.db.models import Sum, Count, Avg

from core.models import Transaction


@dataclass
class ReportParams:
    start_date: datetime.datetime
    end_date: datetime.datetime
    user: User


def transactions_report(params):
    queryset = Transaction.objects.filter(
            user=params.user,
            date__gte=params.start_date,
            date__lte=params.end_date,
        ).values("category__name").annotate(
        total=Sum("amount"),
        count=Count("id"),
        avg=Avg("amount"),
    )

    return queryset
