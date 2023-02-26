import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
planes = []
gate = [0,]
for i in range(P):
    planes.append(int(input()))
for i in range(G):
    gate.append(i+1)

cnt = 0

def union_find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = union_find(parent,parent[x])
    return parent[x]

# def union_find(parent, x):
#     if parent[x] == x:
#         return x
#     return union_find(parent,parent[x])


for g in planes:
    plane = union_find(gate, g)
    if plane == 0:
        break
    else:
        cnt+=1
        gate[plane] = gate[plane-1]
    
    
print(cnt)