from utils.BFS import bfs, bfs_path

N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    a,b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

path = bfs_path(0, N-1, graph, N)

if path:
    print(len(path))
    print(*[x+1 for x in path])
else:
    print("IMPOSSIBLE")