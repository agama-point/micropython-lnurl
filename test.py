import lnurl
from lnurl.lnurlpay import LNURLPay
from lnurl.lnurlwithdraw import LNURLWithdraw

url = "LNURL1DP68GURN8GHJ7MRWW4EXCTNXD9SHG6NPVCHXXMMD9AKXUATJDSKHQCTE8AEK2UMND9HKU0FHXSERSVRZV5UX2VPNV3SNGETYV3SKGVPKXQCRXV3CV5UXXWRR8P3NWDN9XSURSVRP8QCX2VTRV5MXGCFSXCENGE3CVYMXXC34VS6RS2WFRZD"

ln = lnurl.LNURL.from_url(url)
print(ln)

originalurl = lnurl.LNURL.from_lnurl(ln.lnurl).url
print(originalurl)
print(url == originalurl)


lnw = "LNURL1DP68GURN8GHJ7MRWW4EXCTNXD9SHG6NPVCHXXMMD9AKXUATJDSKHW6T5DPJ8YCTH8AEK2UMND9HKU0FHXSERSVRZV5UX2VPNV3SNGETYV3SKGVPKXQCRXV3CV5UXXWRR8P3NWDN9XSURSVRP8QCX2VTRV5MXGCFSXCENGE3CVYMXXC34VS6RSN8LRVA"
lnwcls = LNURLWithdraw.from_url(lnw)
print(lnwcls)

print(lnwcls.init())
print("MIN: {}".format(lnwcls.min_withdrawable))
print("MAX: {}".format(lnwcls.max_withdrawable))


lnpay = "lightning:LNURL1DP68GURN8GHJ7MRWW4EXCTNXD9SHG6NPVCHXXMMD9AKXUATJDSKHW6T5DPJ8YCTH8AEK2UMND9HKU0FCVV6KZC3CVGUKXCMZXCUKXVP5XCURWCMYXYENGCFKXF3R2ERYXP3RVEF4XE3KZVEHXC6N2VPCXUURQEPNXQERJVEEVYCX2VNZXQ6XZDVHQ9F"
lnpaycls = LNURLPay(lnpay)
print(lnpaycls)

print(lnpaycls.init())
print("MIN: {}".format(lnpaycls.min_sendable))
print("MAX: {}".format(lnpaycls.max_sendable))

invoice = lnpaycls.get_invoice(lnpaycls.min_sendable)
print("Invoice: {}".format(invoice))

#print("Pay status: {}".format(lnwcls.pay_invoice(invoice)))
