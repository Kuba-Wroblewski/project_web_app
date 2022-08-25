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
    json.dumps(data, indent=2)

    # data = list(data)
    # print(data)
    print(type(data))

    # for dict in data:
    #     print(data)
    #     if 4.5 < dict['rates'] < 4.7:
    #         print(dict['rates'])

    for dict in data:
        for item in data[dict]:
            for key in item:
                print(item)
            # print(item)

        # for dict in list:
        #    if 4,5 < dict[waluta] < 4,7:
        #       print(dict[data])


