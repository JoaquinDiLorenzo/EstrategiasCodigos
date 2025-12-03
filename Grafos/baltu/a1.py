import sys
from collections import deque

def bfs(start, end, graph, n):
    dist = [-1] * n # se inicializan todos en negativo para empezar
    parent = [-1] * n
    dist[start] = 0
    q = deque([start])

    while q:
        v = q.popleft()
        for to in graph[v]:
            if dist[to] == -1:      # no visitado aún
                dist[to] = dist[v] + 1
                parent[to] = v
                q.append(to)

    if dist[end] == -1:
        return None

    # reconstrucción del camino: end → start usando parent[]
    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        cur = parent[cur]

    path.reverse()

    return dist, path

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    # se agregan los dos
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

# se pide saber si se puede enviar un mensaje desde un nodo hacia otro
# y si es el caso, el minimo numero de nodos en esa ruta
# se va a necesitar el recorrido BFS

res = bfs(0, n-1, graph, n)

if res is None:
    sys.stdout.write("IMPOSSIBLE")
else:
    path = res[1]
    sys.stdout.write(f"{len(path)}\n")
    sys.stdout.write(" ".join(str(x+1) for x in path) + " ")