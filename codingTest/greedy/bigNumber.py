#자연수의 갯수 n, 최대 덧셈횟수 m, 각 이용 횟수 k 입력
#map() 과 input() 그리고 input()을 통해 생성된 객체의 메서드를 사용하는 아래 문장을 잘 이해할 것
n , m , k =map(int,input().split())

#n 개의 수를 입력 받기
data=list(map(int,input().split()))

data.sort() # m >= k 라는 조건이 있기 때문에, 가장 큰 두 수를 k 번씩 서로 번갈아 가면 된다.
bigFirst=data[n-1] # 가장 큰 수
bigSecend=data[n-2] # 다음 큰 수

result=0

while True:
    for i in range(k):
        if m==0:
            break
        result+=bigFirst
        m-=1

    if m==0:
        break
    result+=bigSecend
    m-=1


print(result)
