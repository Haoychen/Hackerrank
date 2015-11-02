__author__ = 'voelunteer'

def BFS(G, s):
    dist = {}
    prev = {}
    explore = {}
    Vertices = G[0]
    Edges = G[1]
    result_list = []
    for node in Vertices:
        dist[node] = -1
        prev[node] = None
        explore[node] = 0
    dist[s] = 0
    explore[s] = 1
    quene = [s]
    while quene != []:
        i = quene.pop(0)
        adjacent_node = [node for node in Vertices if [node, i] in Edges or [i, node] in Edges]
        for node in adjacent_node:
                if explore[node] == 0:
                    dist[node] = dist[i] + 6
                    prev[node] = i
                    quene.append(node)
                    explore[node] = 1
    for node in Vertices:
        if node != s:
            result_list.append(dist[node])
    return result_list

T = int(input())
distances = []
for i in range(T):
    N, M = input().split()
    N, M = int(N), int(M)
    Vertices = list(range(N + 1))
    Vertices.remove(0)
    old_Edges = []
    Edges = []
    for j in range(M):
        old_Edges.append(input().split())
    for edge in old_Edges:
        new_edge = [int(node) for node in edge]
        Edges.append(new_edge)
    G = [Vertices, Edges]
    s = int(input())
    distances.append(BFS(G, s))
for distance in distances:
    for dist in distance:
        print(dist, end = ' ')
    print('\n')

