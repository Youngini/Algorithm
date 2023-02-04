import sys
arr1 = list(sys.stdin.readline())
arr2 = list(sys.stdin.readline())
n, m = len(arr1) - 1, len(arr2) - 1
dp = [0 for _ in range(n)]

for i in range(n):
    k, j = i, 0
    while(j < m):
        if(k == n):
           break
        else:
            if(arr1[k] == arr2[j]):
                dp[i] += 1
                k += 1
                t = j
            else:
                if(j == m - 1):
                    j = t
                    k += 1
        j += 1

print(max(dp))