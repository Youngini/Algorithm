import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr=[]
visited=[]
queue=[]
cnt=[]
for i in range(n):
    number = input().rstrip()
    row = list(map(int,str(number)))
    arr.append(row)
    visited.append([0]*m)
    cnt.append([0]*m)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

queue.append([0,0])
visited[0][0]=1
cnt[0][0]+=1


while(len(queue)>0):
    for k in range(4):
        x = queue[0][1]+dx[k]
        y = queue[0][0]+dy[k]
        if x<m and x>=0 and y<n and y>=0:
            if visited[y][x]==0 and arr[y][x]==1:
                queue.append([y,x])
                cnt[y][x]=cnt[queue[0][0]][queue[0][1]]+1
                visited[y][x]=1
            if (x==m-1 and y==n-1):
                #print(cnt[n-1][m-1])
                break
    queue.pop(0)
    


print(cnt[n-1][m-1])
