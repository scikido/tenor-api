import requests
import json

apikey = "AIzaSyBiialROsFtPSpneAN4F5cl7zgamXRWOWk"  
lmt = 8


search_term = str(input("Search for: ")  )

r = requests.get(
    f"https://g.tenor.com/v1/search?q={search_term}&key={apikey}&limit={lmt}")
# print(f"https://g.tenor.com/v1/search?q={search_term}&key={apikey}&limit={lmt}")
if r.status_code == 200:
    top_8gifs = json.loads(r.content)
    print(top_8gifs)
else:
    top_8gifs = None
    print("Error")

