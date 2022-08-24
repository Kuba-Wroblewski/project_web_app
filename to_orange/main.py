#!/usr/bin/python3

import requests
import time
import json
from threading import Timer


class Request:
    _url = "http://api.nbp.pl/api/exchangerates/rates/a/eur/last/100/?format=json"

    def local_time(self):
        _seconds = time.time()
        _local_time = time.ctime(_seconds)
        return _local_time

    def send_your_request(self):
        _response = requests.get(self._url)
        _text = "1. Sending a GET request to the specified host => "
        return str(_text)

    def response_time(self):
        _start = time.perf_counter()
        _status_code = requests.get(self._url)
        _stop = time.perf_counter()
        _response = "2. Time to receive a response from the host =>", round(_stop - _start, 4)
        return str(_response)

    def response_code(self):
        _status_code = requests.get(self._url)
        _status = "3. HTTP response code =>", _status_code, "2xx - Success Codes"
        return str(_status)

    def is_the_response_is_json(self):
        _validate = requests.get(self._url)
        _validate = "4. If the answer is: JSON =>", _validate.headers['content-type']
        return str(_validate)

    def json_validate(self):
        _r = requests.get(self._url)
        try:
            json.loads(_r.text)
        except ValueError as err:
            print(err)
            return False
        _response = "5. Validated if the JSON has the correct syntax =>", True, self.local_time()
        return str(_response)

    def create_log_file(self):
        for _ in range(1):
            pass
            with open('log.txt', 'a') as f:
                f.write(run.send_your_request()+run.response_time()+run.response_code()+run.is_the_response_is_json()
                        + run.json_validate()+'\n')
                print(run.send_your_request(), run.response_time(), run.response_code(), run.is_the_response_is_json(),
                      run.json_validate())
                f.close()


run = Request()


def time_loop():
    Timer(1, time_loop).start()
    Request().create_log_file()


time_loop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    w = Request()
