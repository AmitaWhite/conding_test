#더해지는 횟수가 수 억번 쯤 된다면

#입력받을 수 (n은 배열의 크기, m은 더하는 횟수, k는 한 숫자당 최대 횟수)
n,m,k=map(int,input().split())

#입력받는 데이터
data=list(map(int,input().split()))

#데이터 정렬
data.sort()

bigFirst=data[n-1]
bigSecend=data[n-2]

count=m//(k+1)

bigF=bigFirst*count*k
bigS=bigSecend*count

lasted=bigFirst*(m%(k+1))

result=0

result=bigF+bigS+lasted

print(result)
