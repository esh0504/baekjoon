import math
testcase=int(input())

def lcm(m,n):
    return int(m*n/math.gcd(m,n))
for i in range(testcase):

    count=0

    m,n,x,y=map(int,input().split())
    a=0
    b=0
    for t in range(lcm(m,n)):
        a=a+1
        b=b+1

        if a>m:
            a=1
        if b>n:
            b=1

        count+=1

        if a==x and b==y:
            print(count)
            break

        if a==m and b==n:
            print(-1)
            break

