array = [7,8,6,9,2,4,5,3,1,0]

for i in range(len(array)):
    min_arr = i
    for j in range(i + 1, len(array)):
        if array[min_arr] >= array[j]:
            min_arr = j

    array[i] , array[min_arr] = array[min_arr], array[i]


print(array)
