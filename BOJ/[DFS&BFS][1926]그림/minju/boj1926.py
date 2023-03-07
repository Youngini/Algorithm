import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

# 상, 하, 좌, 우 방문 여부 확인하는 거 찾아보니까 다들 이렇게 했더라
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    #방문
    graph[a][b] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
                continue
            if graph[next_x][next_y] == 1:
                #방문
                graph[next_x][next_y] = 0
                queue.append((next_x, next_y))
                cnt += 1

    return cnt


paint = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            paint.append(bfs(graph, i, j))


if len(paint) == 0:
    print(len(paint))
    print(0)
else:
    print(len(paint))
    print(max(paint))


