n,m,k= map(int,input().split())
data= list(map(int,input().split()))

data.sort()

bigFirst= data[n-1]
bigSecend= data[n-2]

count= 0

count= m//(k+1)*k
count+= m%(k+1)

result= 0

result= count*bigFirst
result+= (m-count)*bigSecend

print(result)
