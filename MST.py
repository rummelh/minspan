#input: an adjacency matrix
#output: list of tuples
def Prims(G):
    V = list(range(len(G)))
    source = V[0]
    dist = []
    prev = []
    for v in V:
        dist.append(float('inf'))
        prev.append(0)
    dist[source] = 0
    prev[source] = source
    for x in V:
        if G[source][x] != 0:
            dist[x] = G[source][x]
            prev[x] = source
    visited = []
    visited.append(source)
    MST = []
    while(len(visited) < len(V)):
        min_distance = float('inf')
        current_node = None
        for x in range(len(dist)):
            if x not in visited and dist[x] < min_distance:
                min_distance = dist[x]
                min_vertex = x
        current_node = min_vertex
        visited.append(current_node)
        MST.append((prev[current_node],current_node,min_distance))
        for x in V:
            if G[current_node][x] != 0 and x not in visited:
                if G[current_node][x] < dist[x]:
                    dist[x] = G[current_node][x]
                    prev[x] = current_node
    return MST


