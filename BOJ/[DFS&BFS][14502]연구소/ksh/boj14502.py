import sys
import copy
input = sys.stdin.readline

n,m = map(int, input().split())
arr=[]
visited=[]
val=0
total=[]
sum=0
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
    visited.append([0]*m)

select = []
for i in range(n):
    for j in range(m):
        select.append([i,j])

lab = copy.deepcopy(arr)
test = copy.deepcopy(arr)
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def virus(y,x):
    global val
    global lab
    for i in range(4):
        row = y+dy[i]
        col = x+dx[i]
        if row<n and row>=0 and col<m and col>=0:
            if lab[row][col]==0 and visited[row][col]==0:
                visited[row][col]=1
                val+=1
                lab[row][col]=2
                virus(row,col)

def do_sum():
    global sum
    sum=0
    for i in range(n):
        for j in range(m):
            if test[i][j]==0:
                sum+=1
    total.append(sum)


def comb():
    global total
    global lab
    lab = copy.deepcopy(arr)
    for i in range(n*m-2):
        row = select[i][0]
        col = select[i][1]
        if arr[row][col]==0:
            lab[row][col]=1

            for j in range(i+1,n*m-1):
                row = select[j][0]
                col = select[j][1]
                if arr[row][col]==0:
                    lab[row][col]=1

                    for k in range(j+1,m*n):
                        row = select[k][0]
                        col = select[k][1]
                        if arr[row][col]==0:
                            lab[row][col]=1

                            for x in range(n):
                                for y in range(m):
                                    if visited[x][y]==0 and lab[x][y]==2:
                                        visited[x][y]=1
                                        val=1
                                        test = copy.deepcopy(lab)
                                        virus(x,y)
                            do_sum()
                            lab[row][col]=0
                    lab[row][col]=0
            lab[row][col]=0






comb()



print(max(total))