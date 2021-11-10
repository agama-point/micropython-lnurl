from bech32 import bech32_decode, bech32_encode, convertbits

__version__ = "0.0.1"
__license__ = "MIT"


class LNURL():
    def __init__(self):
        pass


    def __str__(self):
        """Return an informal representation suitable for printing."""
        return ("LNURL: '{}' ({})").format(self.value, self.url)


    def __repr__(self):
        return self.__str__()


    @property
    def value(self):
        return self._value


    @value.setter
    def value(self, value):
        self._value = value


    @property
    def url(self):
        if not self.value:
            return None

        parsed = bech32_decode(self._value)[1]
        decoded = convertbits(parsed, 5, 8, False)
        return bytes(decoded).decode()


    @url.setter
    def url(self, value):
        conv = convertbits(value.encode(), 8, 5)
        encoded = bech32_encode("lnurl", conv).upper()
        self._value = encoded


def from_url(url):
    obj = LNURL()
    obj.url = url
    return obj


def from_lnurl(lnurl):
    obj = LNURL()
    obj.value = lnurl
    return obj
