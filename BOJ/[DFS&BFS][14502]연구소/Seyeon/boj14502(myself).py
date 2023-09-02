import sys
from collections import deque
import copy

input = sys.stdin.readline

graph = []

def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph)

    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i,j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            x += nx[i]
            y += ny[i]

            if x<0 or x>=n or y<0 or y>=m:
                continue
            if tmp_graph[x][y] == 0:
                tmp_graph[x][y] = 2
                queue.append((x,y))
    cnt = 0
    global answer

    for i in range(n):
        cnt += tmp_graph[i].count(0)
        
    answer = max(answer, cnt)

def makeWall(cnt):
    if cnt == 3:
        bfs()
        return #벽이 3개가 모두 배치되었으면 makeWall 함수를 종료해야함.

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1)
                graph[i][j] = 0
    

nx = [0, 0, 1, -1]
ny = [1, -1, 0, 0]
 
n, m = map(int, input().split())

answer = 0

for i in range(n):
    graph.append(list(map(int, input().split())))


makeWall(0)
print(answer)

