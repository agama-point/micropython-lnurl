import urequests
from . import LNURL, LNURLException


class LNURLWithdraw(LNURL):
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
            raise LNURLException("Invalid URL, is not withdraw request")

        if data['tag'].lower() != "withdrawrequest":
            raise LNURLException("NOT withdraw request")

        self._callback = data['callback']
        self._k1 = data['k1']

        self.default_description = data['defaultDescription']
        self.min_withdrawable = data['minWithdrawable']
        self.max_withdrawable = data['maxWithdrawable']

        return True


    def reload(self):
        self.init()


    def pay_invoice(self, invoice):
        data = self._callserver("{}?k1={}&pr={}".format(self._callback, self._k1, invoice))

        if "status" in data and data['status'].upper() == "OK":
            return True
