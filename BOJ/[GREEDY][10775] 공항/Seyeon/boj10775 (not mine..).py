import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] == x:
        return x
    P = find_parent(parent[x])
    parent[x] = P
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

G = int(input())
P = int(input())

parent = {i: i for i in range(0, G+1)}
planes = []
count = 0

for _ in range(P):
    planes.append(int(input()))

for plane in planes:
    x = find_parent(plane)

    if x == 0:
        break
    union(x, x-1)
    count += 1

print(count)
