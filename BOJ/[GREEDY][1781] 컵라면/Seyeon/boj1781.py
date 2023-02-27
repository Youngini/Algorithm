import sys
import heapq
input = sys.stdin.readline

n = int(input())

heap = []

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    array[i].reverse() #0열이 컵라면수 , 1열이 데드라인 
array.sort(key=lambda x: (x[0], -x[1]))


for i in range(n):
    print(heap)
    if len(heap) < array[i][1]:
        heapq.heappush(heap,[(-1)*array[i][0],array[i][1]])
    elif abs(heap[0][0]) < array[i][0]:
        heapq.heappop(heap)
        heapq.heappush(heap,[(-1)*array[i][0],array[i][1]])

result = 0
while len(heap)!=0:
    result += heapq.heappop(heap)[0]
print(abs(result))
