from underground import metadata, SubwayFeed

url = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct/gtfs-bdfm"
API_KEY = 'Sk9HMgyQuN24slsbgXEEs2avCkx5pbxr68SxonnD'
ROUTE = 'B'
feed = SubwayFeed.get(ROUTE, api_key=API_KEY)

for key, val in feed.extract_stop_dict().items():
    print(key)
    print('*' * 50)
    for x, y in val.items():
        print(x)
        for val in y:
            print(val)
    break