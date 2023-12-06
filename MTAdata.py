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

  for key, line in enumerate(lines):
    arr = line[str(key)][0]

    for index in range(len(arr) - 1):
      if arr[index] in graph:
        graph[arr[index]].update({ arr[index + 1]: 1})
      else:
        graph[arr[index]] = {}

  for key, line in enumerate(lines):
    arr = line[str(key)][0]

    for index in range(len(arr) - 1)[::-1]:
      if arr[index] in graph:
        graph[arr[index]].update({ arr[index - 1]: 1})
      else:
        graph[arr[index]] = {}
  return graph

def graph_weight(graph):
  for key, line in enumerate(lines):
    arr = line[str(key)][0]

    for index in range(len(arr)):

      for ind, val in feed.extract_stop_dict().items():
        print(ind) # Train

        for x, y in val.items(): 
          print(arr) # Gets the ID of stop

          if x in stopsID:
            if stopsID[x] in arr:
              graph[arr[key][stopsID[x]]] = y[0]

  pprint.pprint(graph)


# def build_graph():
#   graph = {}
#   nextStop = False
#   for key, val in feed.extract_stop_dict().items():
#     for x, y in val.items():
#       if x in stopsID:  
#         if nextStop:
#           graph[prev].update({ stopsID[x] : 1 })
#           nextStop = False
#         if stopsID[x] in graph:
#           prev = stopsID[x]
#           nextStop = True
#         else:
#           graph[stopsID[x]] = {}
#   return graph

# def build_graph():
#   graph = {}
#   for index in range(len(stations) - 1):
#     stationID = stations[index]['GTFS Stop ID']
#     stationName = stations[index]['Stop Name']
#     nextstationID = stations[index + 1]['GTFS Stop ID']
#     nextStationName = stations[index + 1]['Stop Name']

#     if stationID in stopsID and nextstationID in stopsID: 
#       if stationName in graph:
#         graph[stationName].update({ nextStationName : 1 })
#       else:
#         graph[stationName] = {}

#   return graph

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

# # Get the start location time
# # Go to the next stop latest time
# # subtract the start time and last stop time
# # total_time = start_time - nextstop_time 
# # return total_time

# def amount_of_time(start, end):
#   start_time = None

#   for train, stops in feed.extract_stop_dict().items():
#     for stop, times in stops.items():
#       if stop[-1] == "N":
#         time = str(times[0])

#         if stopsID[stop] == start:
#           start_time = datetime.datetime(int(time[:4]), int(time[5:7]), int(time[8:10]), int(time[11:13]), int(time[14:16]), int(time[17:19]))

#         if stopsID[stop] == end and start_time:
#           nextstop_time = datetime.datetime(int(time[:4]), int(time[5:7]), int(time[8:10]), int(time[11:13]), int(time[14:16]), int(time[17:19]))
#           return nextstop_time - start_time

#   return -1

# def subtract_datetime(first, second):
#   first = str(first)
#   second = str(second)
#   start_time = datetime.datetime(int(first[:4]), int(first[5:7]), int(first[8:10]), int(first[11:13]), int(first[14:16]), int(first[17:19]))
#   nextstop_time = datetime.datetime(int(second[:4]), int(second[5:7]), int(second[8:10]), int(second[11:13]), int(second[14:16]), int(second[17:19]))
#   return nextstop_time - start_time


# Take into account North and South
# Only works for one train
# Have to implement a way to check transfers

# with open("graph.json", "w") as outfile: 
#     json.dump(build_graph(), outfile)
# check_MTA_data()
pprint.pprint(build_graph())
# print(amount_of_time("125 St", "145 St"))   