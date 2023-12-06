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
# # # Get the start location time
# # # Go to the next stop latest time
# # # subtract the start time and last stop time
# # # total_time = start_time - nextstop_time 
# # # return total_time
# def amount_of_time(start, end):
#   start_time = None

#   for train, stops in feed.extract_stop_dict().items():
#     for stop, times in stops.items():
#       if stop[-1] == "N":
#         time = str(times[0])
#         if stop in stopsID:
#           if stopsID[stop] == start:
#             start_time = datetime.datetime(int(time[:4]), int(time[5:7]), int(time[8:10]), int(time[11:13]), int(time[14:16]), int(time[17:19]))

#           if stopsID[stop] == end and start_time:
#             nextstop_time = datetime.datetime(int(time[:4]), int(time[5:7]), int(time[8:10]), int(time[11:13]), int(time[14:16]), int(time[17:19]))
#             return nextstop_time - start_time

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