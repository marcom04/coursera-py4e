# Sum numbers inside txt file using regex

import re
import sys

filename = sys.argv[1]
with open(filename) as f:
    text = f.read()
    f.close()

pattern = r'[0-9]+'
results = re.findall(pattern, text)
acc = 0
for num in results:
    acc += int(num)
print(acc)