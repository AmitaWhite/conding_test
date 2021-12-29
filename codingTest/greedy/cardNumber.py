#공백으로 구분되는 행,열 수 입력
row, column = map(int,input().split())

#0인 2차원 리스트 생성
#card = [[0]*column for _ in range(row)]

result=0

for i in range(row):
    data = list(map(int,input().split()))
    min_value=min(data)
    result=max(min_value,result)

print(result)
