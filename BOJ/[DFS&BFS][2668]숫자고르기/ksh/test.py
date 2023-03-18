import sys
input = sys.stdin.readline

n = int(input())
link = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for i in range(1,n+1):
    link[int(input())].append(i)



ans = set()
def dfs(v,stack):
    for i in link[v]:
        if visited[i]:
            while stack: 
                a = stack.pop()
                ans.add(a)
                if i == a:
                    break
            return
        
        visited[i] = True
        dfs(i,stack+[i])
        visited[i] = False
            
for i in range(1,n+1):
    dfs(i,[])
ans = sorted(list(ans))
print(len(ans),*ans,sep='\n')