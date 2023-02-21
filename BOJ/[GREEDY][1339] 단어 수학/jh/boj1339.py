import sys
input = sys.stdin.readline

N = int(input())
ans = []
for _ in range(0,N):
    ans.append(str(input().strip('\n')))


dict1 = {}
num1 = 9
num2=0; sol=0
ans.sort(key=len,reverse=True)

for i in range(1,len(ans)):
    ans[i]= ans[i].zfill(len(ans[0]))

for j in range(0,len(ans[0])):
    for i in range(0,len(ans)):
        if(ans[i][j]!='0' and ans[i][j] not in dict1):
            dict1[ans[i][j]] = num1
            num1-=1

# for i in range(0,len(ans[i])):
#     for j in range(0,len(ans)):
#         if (ans[i][j]!= 0 and ans[i][j] not in dict1):
#             dict1[ans[i][j]] = num1
#             num1-=1

for i in range(0,len(ans)):
    num2=0
    for j in range(0,len(ans[i])):
        if(ans[i][j]!='0'):
            num2*=10
            num2+=dict1.get(ans[i][j])
    sol+=num2

print(sol)
