import sys, heapq
input = sys.stdin.readline

G = int(input())
P = int(input())
gate = [int(input()) for x in range(P)]
count = [0 for _ in range(G)]

for i in gate:
    if(sum(count[:i]) < i):
        count[i - 1] += 1
    else:
        break

print(sum(count))