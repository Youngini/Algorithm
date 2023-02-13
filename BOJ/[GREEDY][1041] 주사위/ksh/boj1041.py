import sys
n = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))
arr=[]

for i in range(3):
    if num_list[i]<num_list[5-i]:
        arr.append(num_list[i])
    else:
        arr.append(num_list[5-i])
arr.sort()

sum=0
buf=arr[0]
sum += (4*(n-1)*(n-2) + (n-2)*(n-2)) * buf
buf+=arr[1]
sum += (4*(n-1) + 4*(n-2)) * buf
buf+=arr[2]
sum += 4 * buf

val=0
if n==1:
    for i in num_list:
        val += i
    val -= max(num_list)
    print(val)
else:
    print(sum)