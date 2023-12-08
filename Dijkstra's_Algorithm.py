import MTAdata

stopGraph = MTAdata.graph_weight(MTAdata.build_graph())
graph = {'a':{'b':10,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}}
 
def dijkstra(graph, start, end):
    shortest_distance = {}
    pre = {}
    unseen = graph
    path = []
    inf = 9999999

    for node in unseen:
        shortest_distance[node] = inf # Gives all nodes a base weight of inf
    shortest_distance[start] = 0 # Start gets 0 since there should be no distance
 
    while unseen:
        min_node = None
        for node in unseen:
            if not min_node:
                if node[:2] == "N " or node[:2] == "S ": # Adjusting string to be a valid key
                    min_node = node[2:]
                else:
                    min_node = node

            elif shortest_distance[node] < shortest_distance[min_node]: # adjust min_node, changes depending which has the least weight
                if node[:2] == "N " or node[:2] == "S ":
                    min_node = node[2:]
                else:
                    min_node = node
 
        for child_node, weight in graph[min_node].items():
            if child_node[:2] == "N " or child_node[:2] == "S ":
                child_node = child_node[2:]

            if weight + shortest_distance[min_node] < shortest_distance[child_node]: # checks the smallest weight value
                shortest_distance[child_node] = weight + shortest_distance[min_node] # gives the smallest weight value to shortest distnace
                pre[child_node] = min_node

        unseen.pop(min_node)
 
    currentNode = end

    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = pre[currentNode]
        except KeyError:
            print('End not reachable')
            break

    path.insert(0, start)

    if shortest_distance[end] != inf:
        print(f'Shortest distance is {shortest_distance[end] // 60} minutes')
        print(f'The path is {path}')
 
 
dijkstra(stopGraph, '168 St-Washington Hts', 'Whitlock Av')