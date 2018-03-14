import requests
import re


with open("1.html","r") as f:
    links=re.findall('<a.*href="([^"]*)"',f.read())
links.sort
print(links)
