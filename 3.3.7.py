import requests
import re

links=[]
res=requests.get(input().strip())
if res.status_code==200:
    for link in re.findall(r'(?:<a.*href=[\"\']+)(?!\.\.)(?:\w*:\/+)?([^\/\'\":]+)',res.text):
        if link not in links and link !='':
            links+=[link]
links.sort()
print("\n".join(links))
