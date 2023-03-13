import sys
sys.setrecursionlimit(10**7)

def dfs(x,y):
    global temp
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        temp += 1
        return True
    return False

n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

result = 0    
maximum = 0
for i in range(n):
    for j in range(m):
        temp = 0
        if dfs(i, j) == True:
            result += 1
            if maximum < temp:
                maximum = temp
print(result)
print(maximum)
