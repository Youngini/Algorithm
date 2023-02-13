import sys

n = int(sys.stdin.readline())

input = []
dp = [1]*(n+1)

for i in range(n):
    input.append(list(map(int, input().split)))

for i in range(n+1):
    if input[i] < input[i+1]:
        dp[i] += 1