import sys
import heapq
input = sys.stdin.readline

n = int(input())

heap = []
array = []

for i in range(n):
    array.append(list(map(int, input().split())))
    
array.sort(reverse = True)


for i in range(n):
    if len(heap) < array[i][0]:
        heapq.heappush(heap,array[i])
    elif heap[0][1] < array[i][1]:
        heapq.heappop(heap)
        heapq.heappush(heap,array[i])

result = 0
while len(heap)!= 0:
   result += heapq.heappop(heap)[1]
   
print(result)
