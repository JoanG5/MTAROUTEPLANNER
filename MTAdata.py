from underground import SubwayFeed
import datetime
import json 
import pprint

url = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct/gtfs-bdfm"
API_KEY = 'Sk9HMgyQuN24slsbgXEEs2avCkx5pbxr68SxonnD'
ROUTE = 'A'
ROUTES = ["H","M","D","1","Z","A","N","GS","SI","J","G","Q","L","B","R","F","E","2","7","W","6","4","C","5","FS"]
feed = SubwayFeed.get(ROUTE, api_key=API_KEY) 

with open('stopsID.json', 'r') as f:
  stopsID = json.load(f)

with open('stations.json', 'r') as f:
  stations = json.load(f)

with open('lines.json', 'r') as f:
  lines = json.load(f)

def build_graph():
  graph = {}

  for key, stops in lines.items():

    for index in range(len(stops) - 1):
      if stops[index] in graph:
        graph[stops[index]][stops[index + 1]] = 1
      else:
        graph[stops[index]] = {}
  
  for key, stops in lines.items():

    for index in range(len(stops) - 1)[::-1]:
      if stops[index] in graph:
        graph[stops[index]][stops[index - 1]] = 1
      else:
        graph[stops[index]] = {}

  return graph

def graph_weight(graph, route):
  feed = SubwayFeed.get(route, api_key=API_KEY) 

  stopTimes = {}
  for train, val in feed.extract_stop_dict().items(): 
    for x, y in val.items(): 
      if x in stopsID:    # Checks if x=(station ID API gives) is in the JSON
        stopTimes[stopsID[x]] = y # Makes the stop the key, and the list of times the value
                                  # ex. "{175th st: [time1, time2, time3 ...] }"
  
  for key, stops in graph.items():
    for stop, weight in stops.items():
      if stop in stopTimes:
        stops[stop] = stopTimes[stop][0]

  return graph

def check_MTA_data():
  for key, val in feed.extract_stop_dict().items():
    print("-" * 100)
    print(key) # Train
    for x, y in val.items(): 
      print()
      print(x) # Gets the ID of stop
      if x in stopsID:
        print(stopsID[x]) # Get the name of Stop
        print()
        for val in y:
          print(val) # Time of the upcoming stops
    break

# with open("graph.json", "w") as outfile: 
#     json.dump(build_graph(), outfile)
# check_MTA_data()
stopGraph = build_graph()
for route in ROUTES:
  stopGraph = graph_weight(stopGraph, route)
  pprint.pprint(stopGraph)

