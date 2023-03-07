import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr=[]
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
