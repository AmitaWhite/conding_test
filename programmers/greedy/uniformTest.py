#테스트 케이스 20개 중 3개에 대해서 통과하지 못함
# FIXME: 여분의 옷을 가지고 있으나 도난 당했을 경우, 자기 옷부터 챙겨야 함
#아래 코드는 없는 애들한테 순서대로 줘서 틀렸음

ls = [_+1 for _ in range(7)]
lost = [1,6,7]
reserve = [1,2,3,7]

for i in lost:
    ls.remove(i)

ls.sort()
print("ls:",ls)

count = len(ls)
print("count : ",count)

for i in lost:
    for j in reserve:
        if j-1 == i or j == i or j+1 == i:
            reserve.remove(j)
            count += 1
            print(count)
            break
print("*"*9)
print(count)
