from bech32 import bech32_decode, bech32_encode, convertbits

__version__ = "0.0.2"
__license__ = "MIT"


class LNURLException(Exception):
    pass


class LNURL():
    def __init__(self):
        self._callback = None


    def __str__(self):
        """Return an informal representation suitable for printing."""
        return ("LNURL: '{}' ({})").format(self.lnurl, self.url)


    def __repr__(self):
        return self.__str__()


    @property
    def lnurl(self):
        return self._lnurl


    @lnurl.setter
    def lnurl(self, lnurl):
        self._lnurl = lnurl


    @property
    def url(self):
        if not self.lnurl:
            return None

        parsed = bech32_decode(self._lnurl)[1]
        decoded = convertbits(parsed, 5, 8, False)
        return bytes(decoded).decode()


    @url.setter
    def url(self, lnurl):
        conv = convertbits(lnurl.encode(), 8, 5)
        encoded = bech32_encode("lnurl", conv).upper()
        self._lnurl = encoded


    @classmethod
    def from_url(cls, url):
        obj = cls()
        obj.url = url
        return obj


    @classmethod
    def from_lnurl(cls, lnurl):
        obj = cls()
        obj.lnurl = lnurl
        return obj
