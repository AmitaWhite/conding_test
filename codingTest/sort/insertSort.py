array = [7,8,6,9,2,4,5,3,1,0]

#삽입 정렬의 특징 : 거의 정렬되어 있는 경우에는 O(N) 시간 으로 빠르게 정렬 가능.
for i in range(1,len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j] , array[j-1] = array[j-1] , array[j]

        else:
            break

print(array)
