# !/usr/bin/python3

import json
from urllib.request import urlopen

_url = "http://api.nbp.pl/api/exchangerates/rates/a/eur/last/100/?format=json"


def checkingUrl(self):
    with urlopen(_url) as f:
        data = f.read()
        data = json.loads(data)
        # json.dumps(data, indent=2)
        for item in data['rates']:
            date = item['effectiveDate']
            price = item['mid']
            if 4.7 < item['mid']:
                date_of_range = date
                print(date_of_range)
            if 4.5 > item['mid']:
                date_of_range += date
                print(date_of_range)
                return date_of_range


if __name__ == '__main__':
    checkingUrl(_url)
