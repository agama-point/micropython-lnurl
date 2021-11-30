import lnurl
from lnurl.lnurlpay import LNURLPay
from lnurl.lnurlwithdraw import LNURLWithdraw

url = "https://example.org/of/some/url"

ln = lnurl.LNURL.from_url(url)
print(ln)

originalurl = lnurl.LNURL.from_lnurl(ln.lnurl).url
print(originalurl)
print(url == originalurl)

lnpay = "https://example.org/of/some/url"
lnpaycls = LNURLPay.from_url(lnpay)

print(type(lnpaycls))
print(lnpaycls.init())

print("MIN: {}".format(lnpaycls.min_sendable))
print("MAX: {}".format(lnpaycls.max_sendable))
invoice = lnpaycls.get_invoice(lnpaycls.min_sendable)
print("Invoice: {}".format(invoice))


lnw = "https://example.org/of/some/url"
lnwcls = LNURLWithdraw.from_url(lnw)

print(type(lnwcls))
print(lnwcls.init())

print("MIN: {}".format(lnwcls.min_withdrawable))
print("MAX: {}".format(lnwcls.max_withdrawable))
print("Pay status: {}".format(lnwcls.pay_invoice(invoice)))
