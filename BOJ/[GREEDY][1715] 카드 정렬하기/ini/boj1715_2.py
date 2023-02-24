import sys
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()
ans = 0

while(len(arr) != 1):
    temp = arr[0] + arr[1]
    del arr[0]
    del arr[0]
    ans += temp
    arr.append(temp)
    arr.sort()

print(ans)