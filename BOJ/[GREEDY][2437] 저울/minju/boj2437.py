#incomplete

import sys

n = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().spli()))

w.sort()

target = 1

for i in w:
    if target < i:
        break
    target += i

print(target)