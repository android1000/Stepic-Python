import sys
import re

for line in sys.stdin:
    print(re.sub(r"\b[Aa]+\b", "argh", line.rstrip(),1))
