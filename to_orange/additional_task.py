""""[Zadanie dodatkowe] Program ma sprawdzić czy ceny EUR w 100 ostatnich notowaniach mieściły się
    w zakresie od 4,5 do 4,7 zł, jeśli się nie mieściły to wykazać w jakich dniach."""
import urllib.request
import json
import requests
from urllib.request import urlopen

url = "http://api.nbp.pl/api/exchangerates/rates/a/eur/last/100/?format=json"
# with urllib.request.urlopen(url) as json_url:
#     data = json.loads(json_url.read().decode())
#     print(json.dumps(data, indent=4, sort_keys=True))


with urlopen(url) as f:
    data = f.read()
    data = json.loads(data)
    # print(json.dumps(data, indent=2))

    data = list(data)
    print(data)
    print(type(data))

    # for key in data:
    #     for key2 in data:
    #         print(data)

    data_str = str(data)
    print(data_str)
    print(type(data_str))

    for key in data:
        # for key2 in data:
        print(key)
        print(data)






"""
r = requests.get(url)
data = json.loads(r.text)
print(data)
# print(data['table'], data['currency'])

print(len(data['list']['']))

# for key in data:
#     for nextkey in data[key]:
#         print(nextkey)
"""