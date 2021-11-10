import lnurl

url = "https://example.org/of/some/url"

ln = lnurl.from_url(url)

print(ln)

originalurl = lnurl.from_lnurl(ln.value).url

print(originalurl)
print(url == originalurl)
