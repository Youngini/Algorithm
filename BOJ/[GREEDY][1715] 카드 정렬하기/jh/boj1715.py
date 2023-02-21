import sys
input = sys.stdin.readline
import heapq
from sys import stdin

N= int(input())
arr = []
ans=0
for _ in range(0,N):
    heapq.heappush(arr,int(input()))

if len(arr)==1:
    print(0)
    exit()

while(len(arr)>1):
    sol = heapq.heappop(arr)+heapq.heappop(arr)
    ans+=sol
    heapq.heappush(arr,sol)

print(ans)

