import sys
import re

for line in sys.stdin:
    print(re.sub(r"\b(\w)(\w)(\w*)\b", r"\2\1\3", line.rstrip()))
