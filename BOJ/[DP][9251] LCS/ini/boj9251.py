import sys
arr1 = list(sys.stdin.readline())
arr2 = list(sys.stdin.readline())
n, m = len(arr1), len(arr2)
dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if(arr1[i - 1] == arr2[j - 1]):
            dp[i][j] = dp[i - 1][j]  + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(max(dp[n - 1]))