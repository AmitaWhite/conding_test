'''
## REVIEW: 예제 배열을 이용한 이해용 구문

lost = [3,4,5,6,7,8]
reserve = [2,3,9]
count = 0

ls = [1 for _ in range(10)]

for i in lost:
    ls[i-1] -= 1

for i in reserve:
    ls[i-1] += 1


print(ls)

for i in range(len(ls)):
    if ls[i] == 0 and i-1 >= 0 and ls[i-1] > 1:
        ls[i] += 1
        ls[i-1] -= 1
        continue

    elif ls[i] == 0 and i+1 <= len(ls) and ls[i+1] > 1:
        ls[i] += 1
        ls[i+1] -= 1
        continue

print(ls)

for i in ls:
    if i >= 1:
        count += 1

print(count)
'''

#실제 제출한 정답
def solution(n, lost, reserve):
    #학생 리스트를 초기화
    ls = [1 for _ in range(n)]
    count = 0

    #체육복이 없는 학생
    for i in lost:
        ls[i-1] -= 1

    #체육복이 있는 학생
    for i in reserve:
        ls[i-1] += 1


    for i in range(len(ls)):
        #체육복이 없고, 리스트를 벗어나지 않으며 여벌이 있는 학생 검색
        if ls[i] == 0 and i-1 >= 0 and ls[i-1] > 1:
            ls[i] += 1
            ls[i-1] -= 1
            continue

        elif ls[i] == 0 and i+1 < len(ls) and ls[i+1] > 1:
            ls[i] += 1
            ls[i+1] -= 1
            continue

    #체육복이 있는 학생        
    for i in ls:
        if i >= 1:
            count += 1

    return count
