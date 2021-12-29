n, p = map(int,input().split())

count=0

while n:
    if n%p == 0:
        n/=p
    else:
        n-=1

    count+=1

print(count-1)
