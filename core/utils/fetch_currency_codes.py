import json

from core.models import Currency

# run in shell
f = open('currency_codes.json')

data = json.load(f)
currencies = []

for code, name in data.items():
    # "RUB", "USD", "EUR" previously added
    if code not in ("RUB", "USD", "EUR"):
        currency = Currency(name=name, code=code)
        currencies.append(currency)

Currency.objects.bulk_create(currencies)

f.close()
