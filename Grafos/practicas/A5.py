from utils.KRUSKAL import kruskal

N,M = map(int, input().split())
edges = []

for _ in range(M):
    a,b,c = map(int, input().split())
    edges.append((c,a-1,b-1))

total_cost, used_edges = kruskal(N, edges)

if used_edges != N-1:
    print("IMPOSSIBLE")
else:
    print(total_cost)