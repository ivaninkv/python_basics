import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r'[aA]+\b', 'argh', line, count=1))
