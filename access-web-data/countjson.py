import urllib.request, urllib.parse, urllib.error
import json
import sys

address = input("Enter location: ")
if len(address) < 1:
    print("Invalid address")
    sys.exit(1)

print('Retrieving', address)
uh = urllib.request.urlopen(address)
data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
comments = info["comments"]
count_sum = 0
for comment in comments:
    count_sum += int(comment["count"])

print("Count:", len(comments))
print("Sum:", count_sum)