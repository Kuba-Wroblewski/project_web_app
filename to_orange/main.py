# !/usr/bin/python3

import requests
import time
import json
from time import sleep


_url = "http://api.nbp.pl/api/exchangerates/rates/a/eur/last/100/?format=json"


class RequestToApi:
    def __init__(self, _url):
        self._url = _url

    def _local_time(self):
        seconds = time.time()
        local_time = time.ctime(seconds)
        return local_time

    def _send_your_request(self):
        response = requests.get(self._url)
        text = "1. Sending a GET request to the specified host => "
        return str(text)

    def _response_time(self):
        start = time.perf_counter()
        status_code = requests.get(self._url)
        stop = time.perf_counter()
        response = "2. Time to receive a response from the host =>", round(stop - start, 4)
        return str(response)

    def _response_code(self):
        status_code = requests.get(self._url)
        status = "3. HTTP response code =>", status_code, "2xx - Success Codes"
        return str(status)

    def is_the_response_is_json(self):
        validate = requests.get(self._url)
        validate = "4. If the answer is: JSON =>", validate.headers['content-type']
        return str(validate)

    def _json_validate(self):
        r = requests.get(self._url)
        try:
            json.loads(r.text)
        except ValueError as err:
            print(err)
            return False
        response = "5. Validated if the JSON has the correct syntax =>", True, self._local_time()
        return str(response)

    def create_log_file(self):
        for i in range(10):
            sleep(5)
            with open('log.txt', 'a') as f:
                f.write(self._send_your_request()+self._response_time()+self._response_code()
                        + self.is_the_response_is_json()+self._json_validate()+'\n')
            file = open('log.txt', 'r')
            lines = file.readlines()
            print(lines[-1].rstrip('\n'))
            file.close()


if __name__ == '__main__':
    run = RequestToApi(_url)
    run.create_log_file()
