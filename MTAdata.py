from underground import SubwayFeed
import datetime
import json 
import pprint

url = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct/gtfs-bdfm"
API_KEY = 'Sk9HMgyQuN24slsbgXEEs2avCkx5pbxr68SxonnD'
ROUTE = 'A'
ROUTES = ["1","2","3","4","5","6","7","A","B","C","D","E","F","G","J","L","M","N","Q","R","W","Z"]
feed = SubwayFeed.get(ROUTE, api_key=API_KEY) 

with open('stopsID.json', 'r') as f:
  stopsID = json.load(f)

with open('stations.json', 'r') as f:
  stations = json.load(f)

with open('lines.json', 'r') as f:
  lines = json.load(f)

def build_graph():
  graph = {}
  count = 0
  for key, stops in lines.items():

    for index in range(len(stops) - 1):
      if stops[index] in graph:
        graph[stops[index]][stops[index + 1]] = 1
      else:
        graph[stops[index]] = {stops[index + 1] : 1}
    count += 1
    if count == 2:
      break

  count = 0
  for key, stops in lines.items():

    for index in range(len(stops) - 1)[::-1]:
      if stops[index] in graph:
        graph[stops[index]][stops[index - 1]] = 1
      else:
        graph[stops[index]] = {stops[index - 1] : 1}
    count += 1
    if count == 2:
      break

  return graph

def graph_weight(graph):
  stopTimes = {}
  for route in ROUTES[:2:]:
    feed = SubwayFeed.get(route, api_key=API_KEY)
    for train, val in feed.extract_stop_dict().items(): 
      for x, y in val.items(): 
        if x in stopsID:    # Checks if x=(station ID API gives) is in the JSON
          stopTimes[stopsID[x]] = y[0] # Makes the stop the key, and the list of times the value
                                    # ex. "{175th st: [time1, time2, time3 ...] }"  
  for key, stops in graph.items(): # Key = stop, stops = all possible stops key can make 
    startTime = stopTimes[key]
    for stop, weight in stops.items(): # stop = {stop : 1}
      if stop in stopTimes:
        endTime = stopTimes[stop]
        stops[stop] = subtract_datetime(endTime, startTime)

  return graph

def check_MTA_data():
  for key, val in feed.extract_stop_dict().items():
    print("-" * 100)
    print(key) # Train ex. "A"
    for x, y in val.items(): 
      print()
      print(x) # Gets the ID of stop
      if x in stopsID:
        print(stopsID[x]) # Get the name of Stop
        print()
        for val in y: # y is a list of times [time1, time2, ...]
          print(val) # Time of the upcoming stops
          break
    break

def subtract_datetime(first, second):
  first = str(first)
  second = str(second)
  start_time = datetime.datetime(int(first[:4]), int(first[5:7]), int(first[8:10]), int(first[11:13]), int(first[14:16]), int(first[17:19]))
  nextstop_time = datetime.datetime(int(second[:4]), int(second[5:7]), int(second[8:10]), int(second[11:13]), int(second[14:16]), int(second[17:19]))
  return nextstop_time - start_time

# with open("graph.json", "w") as outfile: 
#     json.dump(build_graph(), outfile)
# check_MTA_data()
stopGraph = graph_weight(build_graph())
pprint.pprint(stopGraph)

