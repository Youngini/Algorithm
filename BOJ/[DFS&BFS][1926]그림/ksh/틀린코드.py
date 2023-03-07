import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
n,m = map(int, input().split())
arr=[]
visited=[]
cnt=0
size=[0,]
val=0
for i in range(n):
    row = list(map(int,input().split()))
    arr.append(row)
    visited.append([0]*(m))
        

def dfs(i, j):
    global val
    if i+1<n and j<m:
        if arr[i+1][j]==1 and visited[i+1][j]==0:
            visited[i+1][j]=1
            val+=1
            dfs(i+1,j)
    if i-1>=0 and j<m:
        if arr[i-1][j]==1 and visited[i-1][j]==0:
            visited[i-1][j]=1
            val+=1
            dfs(i-1,j)
    if i<n and j+1<m:
        if arr[i][j+1]==1 and visited[i][j+1]==0:
            visited[i][j+1]=1
            val=val+1
            dfs(i,j+1)
    if i<n and j-1>=0:
        if arr[i][j-1]==1 and visited[i][j-1]==0:
            visited[i][j-1]=1
            val+=1
            dfs(i,j-1)

    
    


for i in range(n):
    for j in range(m):
        if visited[i][j]==0 and arr[i][j]==1:
            visited[i][j]=1
            val=1
            dfs(i,j)
            size.append(val)


print(len(size)-1)
print(max(size))
