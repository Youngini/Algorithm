#사이클 찾기 - 1.union_find / 2.dfs
import sys
input = sys.stdin.readline
n = int(input())
adj_list=[[]for i in range(n+1)]
arr=[]
visit=[[]for i in range(n+1)]
start=0
cnt = 0
temp = 0
loc=0
for i in range(1,n+1):
    arr.append(int(input()))
for i in range(n):
    adj_list[arr[i]].append(i+1)
    visit[arr[i]].append(0)


def dfs(node):
    global start
    global cnt
    global temp
    while(visit[node]!=[] and loc<len(visit[node])):
        if visit[node][loc]==0:   #계속 바꿔나가는 과정
            visit[node][loc]=1
            next = adj_list[node][0]
            temp +=1
            loc+=1
            dfs(next)
        else:
            if start == node:
                cnt+=temp




for i in range(1,n+1):
    if visit[i][0]==0:
        start = i
        temp = 0
        dfs(i)

print(cnt)