#최단경로로 물고기 먹으러 가는 경로를 다 더해줘야 함
#종료조건 - 더이상 먹을 수 있는 물고기가 없을때 (다 0이거나 / 다 크거나)
#이미 지나간 자리를 0으로 만듦
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr=[]
cnt = 0
ans = 0
shark = 2
visited=[[0]*n for _ in range(n)]
queue=deque()
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
dx = [0,-1,0,1]
dy = [-1,0,1,0]

def bfs(graph, node):
    global cnt
    global shark
    global ans
    while(len(queue)>0):
        for i in range(4):
            x = queue[0][1] + dx[i]
            y = queue[0][0] + dy[i]
            if x<n and x>=0 and y<n and y>=0:
                #if not visited[y][x]:
                    if graph[y][x]==0:
                        visited[y][x]+=1
                        #cnt+=1
                        queue.append([y,x])
                    elif graph[y][x]==shark:
                        visited[y][x]+=1
                        #cnt+=1
                        graph[y][x]=0
                        queue.append([y,x])
                    elif graph[y][x]<shark:
                        visited[y][x] +=1
                        graph[y][x]=0
                        #cnt+=1
                        shark+=1
                        ans+=cnt
                        cnt=0
                        queue.append([y,x])
        cnt+=1
        queue.popleft()


for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            queue.append([i,j])
            visited[i][j]+=1
            bfs(arr,[i,j])
            break

print(ans)