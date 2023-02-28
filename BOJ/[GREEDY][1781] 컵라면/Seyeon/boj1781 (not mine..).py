import heapq
import sys
input = sys.stdin.readline
array = []

for _ in range(n):
    deadline, ramen = map(int, input().split())
    array.append((deadline, ramen))

array.sort()

queue = []

for i in array:
    heapq.heappush(queue,i[1]) #힙에 컵라면 수 추가
    if i[0] < len(queue): #데드라인이 queue의 길이보다 작다면
        heapq.heappop(queue)

print(sum(queue))
