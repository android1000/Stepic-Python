import requests

url="http://numbersapi.com/"
for i in range(15):
    num=input()
    res=requests.get(url+str(num)+"/math",params={"json": True,})
    if res.status_code==200:
        if res.json()["found"]:
            print("Interesting")
        else:
            print("Boring")
