#-----구현 아이디어-----
#입력 크기를 2차원 배열로 선언하고 좌표를 각각 x, y 딕셔너리로 선언
#이동 계획을 리스트에 저장하고 딕셔너리를 참조하여 움직임

n = int(input())
moveType = {'R':(1,0),'L':(-1,0),'U':(0,-1),'D':(0,1)}

x,y = 1,1

moving=input().split()

for i in range(len(moving)):
#이동 전, 아래에서 map 범위를 벗어나는지 조사하기 위해 x, y 값을 복사한 뒤 연산
    nx, ny = x, y

#-------key point-----
#선언한 딕셔너리의 key를 moving 리스트에서 get 함수로 받은 value를 'value' 리스로 작성
    value = list(moveType.get(moving[i]))

#'value' 리스트 값을 연산
    nx+=value[0]
    ny+=value[1]

#map 범위를 벗어 나는지 조사
    if nx<1 or ny<1 or nx>n or ny>n:
        continue

#조건을 만족하면 좌표 반영
    x,y = nx, ny

print(x,y)
