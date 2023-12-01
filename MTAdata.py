from underground import metadata, SubwayFeed
import json 

url = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct/gtfs-bdfm"
API_KEY = ''
ROUTE = 'A'
feed = SubwayFeed.get(ROUTE, api_key=API_KEY)

with open('stopsID.json', 'r') as f:
  stopsID = json.load(f)

with open('stopsStation.json', 'r') as f:
  stopsStation = json.load(f)

print(len(stopsID))
print(len(stopsStation))

# for key, val in feed.extract_stop_dict().items():
#     for x, y in val.items():
#         if x == "A57S":
#             print(x)
#             for val in y:
#                 print(val)
#         else:
#             break
