from utils.DIJKSTRA import dijkstra

N,M = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    a,b,c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b,c))

dist = dijkstra(0, graph, N)

print(*dist, "")