array = [7,8,6,9,2,4,5,3,1,0]

#퀵 정렬은 데이터가 거의 정렬 되어 있는 경우 느리게 작동한다.
def quick_sort(array,start,end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left = left + 1
        while right > start and array[right] >= array[pivot]:
            right = right - 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

        quick_sort(array,start,right-1)
        quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)
