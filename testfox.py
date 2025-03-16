import requests
from datetime import datetime, timezone 

timestamp = datetime.fromisoformat("YYYY-MM-DDTHH:MM:SS.sssssssss")
print (timestamp)
respond = requests.get("https://api.opensensemap.org/boxes?date=:date&phenomenon=:phenomenon&format=:format")

print (respond.status_code)
print(respond.json())
""" image = respond.json('image')
link = respond.json('link')
print (image, link) """

""" 2025-02-07T15:03:19.162845Z

https://api.opensensemap.org/boxes?date=2025-02-07T15:03:19.162845Z&phenomenon=:phenomenon&format=json """