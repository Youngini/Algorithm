import sys
N = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]
min_arr = [min(arr[0], arr[5]), min(arr[1], arr[4]), min(arr[2], arr[3])]
min_arr.sort()
arr.sort()
ans = 0

if(N == 1):
    ans = sum(arr[:5])

else:
    ans = 4 * sum(min_arr[:3])
    ans += (4 * (N - 2) + 4 * (N - 1)) * sum(min_arr[:2])
    ans += ((N - 2) * (N - 2) + 4 * (N - 2) * (N - 1)) * min_arr[0]

print(ans)