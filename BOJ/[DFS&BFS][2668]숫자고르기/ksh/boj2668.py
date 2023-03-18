#사이클 찾기 - 1.union_find / 2.dfs
import sys
input = sys.stdin.readline
n = int(input())
adj_list=[[]for i in range(n+1)]
visited=[False]*(n+1)

for i in range(1,n+1):
    adj_list[int(input())].append(i)

cycle = []
cnt=0
ans = set()

def dfs(graph, node):
    global cnt
    visited[node] = True
    

    for i in graph[node]:
        if not visited[i]:
            cycle.append(i)
            dfs(graph,i)
            cycle.pop()

        else:
            if cycle[0]==i:
                cnt += len(cycle)
                ans.update(cycle)



for i in range(1,n+1):
    if not visited[i]:
        cycle.append(i)
        dfs(adj_list,i)
        cycle.pop()




print(cnt)
answer = sorted(list(ans))

for i in answer:
    print(i)




