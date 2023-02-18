import sys

n = int(sys.stdin.readline())
limit = list(map(int, sys.stdin.readline().split()))
limit.sort(reverse = True)

m = int(sys.stdin.readline())
weight = list(map(int, sys.stdin.readline().split()))
weight.sort(reverse = True)

array = [0] * n

i = 0
q = 0
for i in range(m):
    if weight[i] <= limit[(i+n-q)%n]:
        array[(i+n-q)%n] += 1
    else:
        for j in range((i+n-q)%n):
            if weight[i] <=limit[j]:
                array[j] += 1
                q = (i+n+q)%n - j
                break

if max(array) == 0:
    print(-1)
else: print(max(array))
