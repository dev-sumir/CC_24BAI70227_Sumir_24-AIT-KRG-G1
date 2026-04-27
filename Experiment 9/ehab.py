import sys
input = sys.stdin.readline

n = int(input())
edges = []
deg = [0]*(n+1)

for _ in range(n-1):
    u, v = map(int, input().split())
    edges.append((u, v))
    deg[u] += 1
    deg[v] += 1

# find node with degree >= 3
node = -1
for i in range(1, n+1):
    if deg[i] >= 3:
        node = i
        break

res = [-1]*(n-1)

if node == -1:
    # simple path
    for i in range(n-1):
        res[i] = i
else:
    label = 0
    
    # assign 0,1,2 to edges connected to node
    for i in range(n-1):
        u, v = edges[i]
        if u == node or v == node:
            if label < 3:
                res[i] = label
                label += 1
    
    # assign remaining labels
    for i in range(n-1):
        if res[i] == -1:
            res[i] = label
            label += 1

print(*res)
