이렇게 쓰니까 답은 맞는데 런타임에러

n = int(input())
sum = 1

def factorial(n):
    if(n>1): return n * factorial(n-1)
    else: return 1

for i in range(2,n,2):
    a = factorial(n-(i/2))
    b = factorial(i/2)
    c = factorial(n-(i/2)-(i/2))
    sum+=a/(b*c)

if(n==2): sum=2
print(int(sum))


---

재귀를 이용한 top-down

n = int(input())

def tile(n):
    if(n>2):
        return tile(n-1) + tile(n-2)
    elif(n==2): return 2
    elif(n==1): return 1
    elif(n==0): return 0


ans = tile(n)
print(ans%10007)

시간초과 --> 배열을 만들어서 하향식으로 메모리뭐시기로