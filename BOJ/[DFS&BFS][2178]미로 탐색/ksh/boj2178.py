import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr=[]
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

#미로의 정보를 저장하려면 dfs를 이용해야함