import re
import sys

pattern = "^(0|(1(01*0)*1))*$"
pattern = re.compile(pattern)
re.compile()
for line in sys.stdin:
    line = line.rstrip()
    if pattern.match(line):
        print(line)
