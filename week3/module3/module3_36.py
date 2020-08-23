import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r'human', 'computer', line))
