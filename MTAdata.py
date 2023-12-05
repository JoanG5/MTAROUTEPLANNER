from underground import SubwayFeed
import datetime
import json 

url = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct/gtfs-bdfm"
API_KEY = 'Sk9HMgyQuN24slsbgXEEs2avCkx5pbxr68SxonnD'
ROUTE = 'A'
feed = SubwayFeed.get(ROUTE, api_key=API_KEY)

with open('stopsID.json', 'r') as f:
  stopsID = json.load(f)

def check_MTA_data():
  for key, val in feed.extract_stop_dict().items():
      print("-" * 100)
      print(key) # Train
      for x, y in val.items():
        if x[-1] == "N":
          print()
          print(x) # Gets the ID of stop
          print(stopsID[x]) # Get the name of Stop
          print()
          for val in y:
            print(val) # Time of the upcoming stops 
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

# Take into account North and South
# Only works for one train
# Have to implement a way to check transfers

check_MTA_data()
print(amount_of_time("125 St", "145 St"))      
