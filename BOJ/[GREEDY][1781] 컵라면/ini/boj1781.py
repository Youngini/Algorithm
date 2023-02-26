import sys, heapq
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
queue = [] # 컵라면 수 저장

for i in arr:
    if(len(queue) < i[0]):
        heapq.heappush(queue, i[1])
    else:
        heapq.heappop(queue)
        heapq.heappush(queue, i[1])

print(sum(queue))