import sys
N, M = map(int,sys.stdin.readline().split())
arr = [int(x) for x in sys.stdin.readline().split()]
positive = []
negative = []
ans = 0

for i in arr:
    if(i > 0):
        positive.append(i)
    else:
        negative.append(i)

positive.sort(reverse = True)
negative.sort()

if(len(negative) == 0): # 음수 없음
    ans += positive[0]
elif(len(positive) == 0): # 양수 없음
    ans += abs(negative[0])
elif(abs(negative[0]) > positive[0]): # 음수 절대값이 더 커
    ans += abs(negative[0]) + 2 * abs(positive[0])
else: #양수 절대값이 더 큼
    ans += 2 * abs(negative[0]) + abs(positive[0])

i = 1
j = 1

while(len(positive) != 1 and i * M < len(positive)):
    j = i * M
    if(j > len(positive)):
        ans += positive[-1] * 2
    else:
        ans += positive[j] * 2
    i += 1

i = 1
j = 1

while(len(negative) != 1 and i * M < len(negative)):
    j = i * M
    if(j > len(negative)):
        ans += negative[-1] * 2
    else:
        ans += negative[j] * 2
    i += 1

print(ans)