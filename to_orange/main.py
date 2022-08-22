import requests
import time
import json
from threading import Timer


class Work:
    def __init__(self):
        self.url = "http://api.nbp.pl/api/exchangerates/rates/a/eur/last/100/?format=json"

    #  local time
    def local_time(self):
        seconds = time.time()
        local_time = time.ctime(seconds)
        return local_time

    # 1. wysłanie żądania na host;
    def send_your_request(self):
        response = requests.get(self.url)
        text = ('1. Sending a GET request to the specified host => ')
        return str(text)

    # 2. Mierzył czas od wysłania żądania do czasu otrzymania odpowiedzi;
    def response_time(self):
        start = time.perf_counter()
        self.status_code = requests.get(self.url)
        stop = time.perf_counter()
        response = ('2. Time to receive a response from the host =>', round(stop - start, 6))
        return str(response)

    # 3. Sprawdź kod odpowiedzi HTTP;
    def response_code(self):
        status_code = requests.get(self.url)
        status = ('3. HTTP response code =>', status_code, '2xx - Success Codes')
        return str(status)

    # 4. Sprawdzał czy odpowiedź to JSON (Content-Type);
    def is_the_response_is_JSON(self):
        validate = requests.get(self.url)
        validate = ('4. If the answer is: JSON =>', validate.headers['content-type'])
        return str(validate)

    # 5. Walidował czy JSON z odpowiedzi ma prawidłową składnię;
    def json_validate(self):
        r = requests.get(self.url)
        try:
            json.loads(r.text)
        except ValueError as err:
            print(err)
            return False
        response = '5. Validated if the JSON has the correct syntax =>', True, self.local_time()
        return str(response)

    # tworzenie pliku log.txt
    def create_log_file(self):
        x = 0
        while True:
            x += 1
            if x > 10:
                break
            with open('log.txt', 'a') as f:
                f.write(w.send_your_request()+w.response_time()+w.response_code()+w.is_the_response_is_JSON()
                        + w.json_validate()+'\n')
                print(w.send_your_request(), w.response_time(), w.response_code(), w.is_the_response_is_JSON(),
                      w.json_validate())
                f.close()


w = Work()


def hello():
    Timer(5, hello).start()
    Work().create_log_file()


hello()


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
