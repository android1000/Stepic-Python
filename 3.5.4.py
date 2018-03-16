import requests
import json

client_id = 'db311cfe37ec4bc74a61'
client_secret = 'ba1d22427d386b0b79ce4403c063b2ec'
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
j = json.loads(r.text)
token = j["token"]
headers = {"X-Xapp-Token" : token}

artists={}
year_artist=[]
for i in range(15):
    artist_id=input()
    r = requests.get("https://api.artsy.net/api/artists/"+artist_id, headers=headers)
    j = json.loads(r.text)
    if j["birthday"] not in artists:
        artists[j["birthday"]]=[]
    artists[j["birthday"]]+=[j["sortable_name"]]
    year_artist+=[j["birthday"]]
#print(artists.keys().sort())
print(artists)
year_artist.sort()
for art in year_artist:
    art_in_year=artists.get(art)
    art_in_year.sort
    print(*art_in_year)
