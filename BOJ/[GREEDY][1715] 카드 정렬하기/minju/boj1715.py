#incomplete

import sys

n = int(sys.stdin.readline())
card_list = []
result_list = []
result = 0
cnt = 0

for _ in range(n):
    card = int(sys.stdin.readline())
    card_list.append(card)

card_list.sort()

if len(card_list) == 1:
    print(0)
else:
    while len(card_list) != 1:
        cnt = card_list[0] + card_list[1]
        card_list.remove(card_list[0])
        card_list.remove(card_list[0])
        card_list.append(cnt)
        result_list.append(cnt)
        card_list.sort()

    print(sum(result_list))


