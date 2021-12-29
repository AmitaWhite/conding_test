#데이터의 크기 범위가 제한되어 정수 형태로 표현 될 때만 사용 가능
#모든 데이터 >= 0
array = [7,2,2,4,5,9,2,1,0,0,9,3,6,7,8]

#최대 크기의 데이터 길이로 리스트 생성 후 0으로 초기화
#array 의 최대 값이 9 이므로 0~9 까지 len(count) == 10 인 리스트 새성
count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

#출력

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end='')
