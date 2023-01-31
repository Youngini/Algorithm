n = int(input())

arr = [0 for j in range(n+1)]
arr[0]=0
arr[1]=1
if(n>1):
    arr[2]=2

for i in range(3,n+1):
    arr[i] = arr[i-1]+arr[i-2]



print(arr[n]%10007)