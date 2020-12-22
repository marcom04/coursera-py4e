import re
import sys
print( sum( [ int(x) for x in re.findall('[0-9]+',open(sys.argv[1]).read()) ] ) )