import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))

# Retrieve all of the anchor tags
print("Retrieving: ", url)
tags = soup('a')
for i in range(count):
    url = tags[pos-1].get('href', None)
    print("Retrieving: ", url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

