import sys, heapq
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
heapq.heapify(arr)

ans = 0
temp = 0

if(N != 1):
    ans = heapq.heappop(arr) + heapq.heappop(arr)
    heapq.heappush(arr, ans)
    while(len(arr) != 1):
        temp = heapq.heappop(arr) + heapq.heappop(arr)
        ans += temp
        heapq.heappush(arr, temp)

print(ans)
