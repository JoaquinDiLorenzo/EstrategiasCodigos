from utils.DSU import DSU

N, M = map(int, input().split())
dsu = DSU(N)
cant = N       
max_size = 1        

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1          
    b -= 1
    if dsu.find(a) != dsu.find(b):
        dsu.union(a, b)
        cant -= 1
        max_size = max(max_size, dsu.size(dsu.find(a)))

    print(cant, max_size)
