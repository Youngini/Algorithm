import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr=[]
visited=[]
stack=[]
for i in range(n):
    number = input().rstrip()
    row = list(map(int,str(number)))
    arr.append(row)
    visited.append([0]*m)

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def dfs(i,j):
    
    for k in range(4):
        x = j+dx[k]
        y = i+dy[k]
        if x<m and x>=0 and y<n and y>=0:
            if visited[y][x]==0 and arr[y][x]==1:
                stack.append([y,x])
                visited[y][x]=1
                if x==m-1 and y ==n-1:
                    print(len(stack))
                    exit
                dfs(y,x)
                
    else:
        stack.pop()


for i in range(n):
    for j in range(m):
        if visited[i][j]==0 and arr[i][j]==1:
            stack.append([i,j])
            visited[i][j]=1
            dfs(i,j)

#print(len(stack))
