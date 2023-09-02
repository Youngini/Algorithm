import sys
input = sys.stdin.readline

same = []

def makeGraph():
    global same
    
    graph = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1,n+1):
        array[i] = int(input())

    for i in range(1,n+1):
        if i == array[i]:
             graph[i].append(i)
             same.append(i)
             
        elif array[array[i]] == i:
            graph[i].append(array[i])
            graph[array[i]].append(i)
            
    return graph

def dfs(graph, v, visited):
    global temp
    global cnt
    cnt += 1
    temp.append(v)
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n = int(input())

array = [0] * (n+1)
graph = makeGraph()
visited = [False] * 9
answer = 0
result = []

for i in range(1,n+1):
    temp = []
    cnt = 0
    dfs(graph, i, visited)
    if answer < cnt:
        answer = cnt
        result = temp
        
print(answer)
result.remove(0)
result += same
result.sort()
for i in range(len(result)):
    print(result[i])
                   
