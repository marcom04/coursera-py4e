import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import sys

address = input("Enter location: ")
if len(address) < 1:
    print("Invalid address")
    sys.exit(1)

print('Retrieving', address)
uh = urllib.request.urlopen(address)
data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
counts = tree.findall('.//count')
count_sum = 0
for count in counts:
    count_sum += int(count.text)

print("Count:", len(counts))
print("Sum:", count_sum)
