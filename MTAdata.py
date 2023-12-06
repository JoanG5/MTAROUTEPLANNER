from underground import SubwayFeed
import datetime
import json 

url = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct/gtfs-bdfm"
API_KEY = 'Sk9HMgyQuN24slsbgXEEs2avCkx5pbxr68SxonnD'
ROUTE = 'A'
feed = SubwayFeed.get(ROUTE, api_key=API_KEY) 

with open('stopsID.json', 'r') as f:
  stopsID = json.load(f)

transfers = []

with open('transfers.txt', 'r') as f:
  for line in f:
    line = line.strip()
    line = line.split(",")
    transfers.append(line)
# def build_graph():
#   graph = {}
#   nextStop = False
#   for key, val in feed.extract_stop_dict().items():
#     for x, y in val.items():
#       if nextStop:
#         graph[prev].update({ stopsID[x] : 1 })
#         nextStop = False
#       if stopsID[x] in graph:
#         prev = stopsID[x]
#         nextStop = True
#       else:
#         graph[stopsID[x]] = {}
#   return graph

# def build_graph():
#   graph = {}
#   for transfer in transfers:
#     if transfer[0] == transfer[1]:
#       continue
#     if transfer[0] in graph:
#       graph[stopsID[transfer[0]]].update( {stopsID[transfer[1]]: 1})
#     else:
#       graph[stopsID[transfer[0]]] = {stopsID[transfer[1]]}
#   return graph

def build_graph():
    graph = {}
    stopsID = {}  # Assuming stopsID is defined somewhere

    for key, val in feed.extract_stop_dict().items():
        for x, y in val.items():
            if stopsID[x] not in graph:
                graph[stopsID[x]] = {}

            connections = graph[stopsID[x]]

            for neighbor, weight in connections.items():
                if stopsID[x].endswith('N') and neighbor.endswith('S'):
                    # Skip connections between northbound and southbound stations
                    continue
                elif stopsID[x].endswith('S') and neighbor.endswith('N'):
                    # Skip connections between southbound and northbound stations
                    continue

            if neighbor in connections:
                connections[neighbor] += 1
            else:
                connections[neighbor] = 1

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
      # for val in y:
      #   print(val) # Time of the upcoming stops
    break
      


# Get the start location time
# Go to the next stop latest time
# subtract the start time and last stop time
# total_time = start_time - nextstop_time 
# return total_time
def amount_of_time(start, end):
  start_time = None

  for train, stops in feed.extract_stop_dict().items():
    for stop, times in stops.items():
      if stop[-1] == "N":
        time = str(times[0])

        if stopsID[stop] == start:
          start_time = datetime.datetime(int(time[:4]), int(time[5:7]), int(time[8:10]), int(time[11:13]), int(time[14:16]), int(time[17:19]))

        if stopsID[stop] == end and start_time:
          nextstop_time = datetime.datetime(int(time[:4]), int(time[5:7]), int(time[8:10]), int(time[11:13]), int(time[14:16]), int(time[17:19]))
          return nextstop_time - start_time

  return -1

def subtract_datetime(first, second):
  # Take into account North and South
  # Only works for one train
  # Have to implement a way to check transfers
  first = str(first)
  second = str(second)
  start_time = datetime.datetime(int(first[:4]), int(first[5:7]), int(first[8:10]), int(first[11:13]), int(first[14:16]), int(first[17:19]))
  nextstop_time = datetime.datetime(int(second[:4]), int(second[5:7]), int(second[8:10]), int(second[11:13]), int(second[14:16]), int(second[17:19]))
  return nextstop_time - start_time


print(build_graph())
# check_MTA_data()