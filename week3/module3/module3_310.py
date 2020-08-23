import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    if re.match(r'^((((0+)?1)(10*1)*0)(0(10*1)*0|1)*(0(10*1)*(1(0+)?))|(((0+) \
                 ?1)(10*1)*(1(0+)?)|(0(0+)?)))$', line):
        print(line)
