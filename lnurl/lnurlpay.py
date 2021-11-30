import urequests
from . import LNURL, LNURLException


class LNURLPay(LNURL):
    def __init__(self):
        super().__init__()


    def _callserver(self, url):
        response = urequests.get(url)

        if response.status_code is not 200:
            sc = response.status_code
            sr = response.text
            response.close()
            raise LNURLException("Bad status code {}: {}".format(sc, sr))

        data = response.json()

        if 'status' in data and data['status'] == 'ERROR':
            raise LNURLException(data['reason'])

        return data


    def init(self):
        data = self._callserver(self.url)

        if "tag" not in data:
            raise LNURLException("Invalid URL, is not pay requests")

        if data['tag'].lower() != "payrequest":
            raise LNURLException("NOT pay request")

        self._callback = data['callback']
        self.min_sendable = data['minSendable']
        self.max_sendable = data['maxSendable']

        return True


    def reload(self):
        self.init()


    def get_invoice(self, amount):
        data = self._callserver("{}?amount={}".format(self._callback, amount))
        return data['pr']
