import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
gate = [0] * P
check = [0] *(G+1)

for i in range(P):
    gate[i] = int(input())
    
result = 0

for i in range(P):
    maximum = gate[i]
    while maximum != 0:
        if check[maximum] == 0:
            check[maximum] = 1
            result += 1
            break
        maximum -= 1
    if maximum == 0:
            break
        
print(result)
