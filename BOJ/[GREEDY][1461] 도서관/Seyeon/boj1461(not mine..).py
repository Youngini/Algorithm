import sys

n, m = map(int, sys.stdin.readline().split())
book = list(map(int, sys.stdin.readline().split()))

negative = []
positive = []

for i in book:
    if i < 0:
        negative.append(i)
    elif i > 0:
        positive.append(i)

distance = []
negative.sort()
for i in range(len(negative)//m):
    distance.append(abs(negative[m*i]))
if len(negative) % m > 0:
    distance.append(abs(negative[(len(negative)//m)*m]))

positive.sort(reverse = True)
for i in range(len(positive)//m):
    distance.append(positive[m*i])
if len(positive) % m > 0:
    distance.append(positive[(len(positive)//m)*m])

distance.sort()
result = distance.pop()
result += 2*sum(distance)
print(result)
