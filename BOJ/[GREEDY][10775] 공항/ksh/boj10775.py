#배열 주소값 접근할 수 있는 방법
import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
planes = []
gate = []
for i in range(P):
    planes.append(int(input()))
for i in range(G):
    gate.append(i+1)

cnt = 0

for g in planes:
    if gate[g-1]==0:
        break

    cnt+=1
    if gate[g-1]==g:
        if g-1 == 0:
            gate[g-1] = 0
        else:
            gate[g-1] = gate[g-2]
    else:
        gate[g-1] = gate[gate[g-1]]
    
print(cnt)