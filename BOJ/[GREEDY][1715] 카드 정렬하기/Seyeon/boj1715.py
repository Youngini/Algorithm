import sys
import heapq
n = int(sys.stdin.readline())

heap = []
for i in range(n):
    heapq.heappush(heap,int(sys.stdin.readline()))

total = 0

if n!=1:
    while len(heap)!=0:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        total += (a+b)
        if len(heap)!=0:
            heapq.heappush(heap,(a+b))

print(total)
