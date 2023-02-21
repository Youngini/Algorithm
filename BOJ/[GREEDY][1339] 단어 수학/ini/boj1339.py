import sys
from collections import defaultdict
N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline()) for _ in range(N)]
arr.sort(key = lambda x : len(x), reverse = True)
ans = 0

alphabet = defaultdict(int)
for i in range(N):
    for j in range(len(arr[i]) - 1):
        alphabet[arr[i][j]] += 10**(len(arr[i]) - 2 - j)

value = list(alphabet.values())
value.sort(reverse = True)

for i in range(len(value)):
    ans += value[i] *(9 - i)

print(ans)