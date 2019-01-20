MAX_DISTANCE = 9999999999



def dijkstra(graph, source):
    distance_to = initialize_weigths(graph, source)

    for vertex in graph.vertices:
        for edge in graph.edges:
            if vertex not in edge:
                continue

            if vertex == edge[0]:
                target = edge[1]
            else:
                target = edge[0]

            if distance_to[target] > distance_to[vertex] + 1:
                distance_to[target] = distance_to[vertex] + 1

    return distance_to

def initialize_weigths(graph, source):
    '''
    Distance matrix from source to any other vertex. Returns a dictionary with the distances from source to any vertex.
    '''

    global MAX_DISTANCE

    distance_to = {}
    for vertex in graph.vertices:
        distance_to[vertex] = MAX_DISTANCE
    distance_to[source] = 0

    return distance_to

def prim():
    pass

def kruskal():
    pass
