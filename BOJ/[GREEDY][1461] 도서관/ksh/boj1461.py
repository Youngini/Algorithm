n, m = map(int, input().split())
num_list = list(map(int, input().split()))
sum=0
pos=[]
neg=[]

for i in range(n):
    if(num_list[i]>0):
        pos.append(num_list[i])
    else:
        neg.append(num_list[i])

pos.sort(reverse=True)
neg.sort()

for i in range(0,len(pos),m):
    sum+=pos[i]*2
for i in range(0,len(neg),m):
    sum-=neg[i]*2

#IndexError
neg.append(0)
pos.append(0)

if abs(neg[0])>pos[0]:
    sum+=neg[0]
else:
    sum-=pos[0]

print(sum)