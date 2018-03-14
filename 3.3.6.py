import requests
import re


urlA=input()
urlB=input()
result="No"
resA=requests.get(urlA)
links=re.findall('<a.*href="([^"]*)"',resA.text)
if resA.status_code==200:
    for link in links:
        resC=requests.get(link)
        links2=links=re.findall('<a.*href="([^"]*)"',resC.text)
        if resC.status_code==200 and urlB in links2 :
            result="Yes"
            break
print(result)
