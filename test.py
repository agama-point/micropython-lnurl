import unittest

from lnurl import LNURL
from lnurl.lnurlpay import LNURLPay
from lnurl.lnurlwithdraw import LNURLWithdraw


class TestLNURL(unittest.TestCase):
    prefixlnurl = "lightning:LNURL1DP68GURN8GHJ7MRWW4EXCTNXD9SHG6NPVCHXXMMD9AKXUATJDSKHQCTE8AEK2UMND9HKU0FHXSERSVRZV5UX2VPNV3SNGETYV3SKGVPKXQCRXV3CV5UXXWRR8P3NWDN9XSURSVRP8QCX2VTRV5MXGCFSXCENGE3CVYMXXC34VS6RS2WFRZD"
    lnurl = "LNURL1DP68GURN8GHJ7MRWW4EXCTNXD9SHG6NPVCHXXMMD9AKXUATJDSKHQCTE8AEK2UMND9HKU0FHXSERSVRZV5UX2VPNV3SNGETYV3SKGVPKXQCRXV3CV5UXXWRR8P3NWDN9XSURSVRP8QCX2VTRV5MXGCFSXCENGE3CVYMXXC34VS6RS2WFRZD"
    url = "https://lnurl.fiatjaf.com/lnurl-pay?session=74280be8e03da4eddad0600328e8c8c8c76e4880a80e1ce6da0634f8a6cb5d48"

    def test_from_url(self):
        ln = LNURL(self.url)
        self.assertEqual(ln.lnurl, self.lnurl, "Should be {}".format(self.lnurl))


    def test_from_lnurl(self):
        ln = LNURL(self.lnurl)
        self.assertEqual(ln.url, self.url, "Should be {}".format(self.url))


    def test_from_prefixlnurl(self):
        ln = LNURL(self.prefixlnurl)
        self.assertEqual(ln.url, self.url, "Should be {}".format(self.url))
        self.assertEqual(ln.lnurl, self.lnurl, "Should be {}".format(self.url))


class TestLNURLPay(unittest.TestCase):
    url = "https://lnurl.fiatjaf.com/lnurl-pay?session=74280be8e03da4eddad0600328e8c8c8c76e4880a80e1ce6da0634f8a6cb5d48"

    def __init__(self):
        self.ln = LNURLPay(self.url)


    def test_parse(self):
        lnurl = "LNURL1DP68GURN8GHJ7MRWW4EXCTNXD9SHG6NPVCHXXMMD9AKXUATJDSKHQCTE8AEK2UMND9HKU0FHXSERSVRZV5UX2VPNV3SNGETYV3SKGVPKXQCRXV3CV5UXXWRR8P3NWDN9XSURSVRP8QCX2VTRV5MXGCFSXCENGE3CVYMXXC34VS6RS2WFRZD"
        self.assertEqual(self.ln.lnurl, lnurl)


    def test_call_init(self):
        init = self.ln.init()
        self.assertTrue(init)
        self.assertIsNotNone(self.ln.min_sendable)
        self.assertIsNotNone(self.ln.max_sendable)


    def test_get_invoice(self):
        inv = self.ln.get_invoice(100)
        self.assertIsNotNone(inv)


class TestLNURLWithdraw(unittest.TestCase):
    url = "https://lnurl.fiatjaf.com/lnurl-withdraw?session=74280be8e03da4eddad0600328e8c8c8c76e4880a80e1ce6da0634f8a6cb5d48"

    def __init__(self):
        self.ln = LNURLWithdraw(self.url)


    def test_parse(self):
        lnurl = "LNURL1DP68GURN8GHJ7MRWW4EXCTNXD9SHG6NPVCHXXMMD9AKXUATJDSKHW6T5DPJ8YCTH8AEK2UMND9HKU0FHXSERSVRZV5UX2VPNV3SNGETYV3SKGVPKXQCRXV3CV5UXXWRR8P3NWDN9XSURSVRP8QCX2VTRV5MXGCFSXCENGE3CVYMXXC34VS6RSN8LRVA"
        self.assertEqual(self.ln.lnurl, lnurl)


    def test_call_init(self):
        init = self.ln.init()
        self.assertTrue(init)
        self.assertIsNotNone(self.ln.min_withdrawable)
        self.assertIsNotNone(self.ln.max_withdrawable)


class TestPayFlow(unittest.TestCase):
    payurl = "https://lnurl.fiatjaf.com/lnurl-pay?session=74280be8e03da4eddad0600328e8c8c8c76e4880a80e1ce6da0634f8a6cb5d48"
    withurl = "https://lnurl.fiatjaf.com/lnurl-withdraw?session=74280be8e03da4eddad0600328e8c8c8c76e4880a80e1ce6da0634f8a6cb5d48"

    def __init__(self):
        self.lnp = LNURLPay(self.payurl)
        self.lnw = LNURLWithdraw(self.withurl)


    def test_call_init(self):
        self.assertTrue(self.lnp.init())
        self.assertTrue(self.lnw.init())


    def test_get_invoice(self):
        self.invoice = self.lnp.get_invoice(self.lnp.min_sendable)
        self.assertIsNotNone(self.invoice)


    def test_pay_invoice(self):
        self.assertTrue(self.lnw.pay_invoice(self.invoice))


if __name__ == "__main__":
    unittest.main()