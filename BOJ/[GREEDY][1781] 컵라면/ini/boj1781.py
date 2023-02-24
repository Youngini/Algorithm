import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
arr.sort(key = lambda x :( x[0], -x[1]))

n, ans = 0, 0

for i in arr:
    if(n < i[0]):
        ans += i[1]
        n = i[0]

print(ans)