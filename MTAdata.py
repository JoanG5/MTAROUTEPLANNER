from underground import SubwayFeed
import datetime
import json 
import pprint

url = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct/gtfs-bdfm"
API_KEY = 'Sk9HMgyQuN24slsbgXEEs2avCkx5pbxr68SxonnD'
ROUTE = 'A'
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

def graph_weight(graph):
    stopTimes = {}
    for train, val in feed.extract_stop_dict().items():
      for x, y in val.items(): 
        if x in stopsID:
          stopTimes[stopsID[x]] = y
    
    for key, stops in graph.items():
      for stop, weight in stops.items():
        if stop in stopTimes:
          stops[stop] = stopTimes[stop][0]
    pprint.pprint(graph)

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
graph_weight(build_graph())

