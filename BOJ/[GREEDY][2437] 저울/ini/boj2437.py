import sys
N = int(sys.stdin.readline())
weight = [int(x) for x in sys.stdin.readline().split()]
weight.sort()
ans = 0

for i in weight:
    if(ans + 1 < i):
        break
    ans += i

print(ans + 1)