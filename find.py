
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
j=1
while j<=8:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    lst = url.split('_')
    na = lst[2].split('.')
    name = na[0]
    i=0
    tags = soup('a')
    for tag in tags:
        lin = tag.get('href', None)
        i = i+1
        if i==18:
            break
    print(name)
    url = lin
    j = j+1
