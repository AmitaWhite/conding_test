def quick_sort2(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort2(left) + [pivot] + quick_sort2(right)


array = [2,4,6,3,9,10,8,7]

print(quick_sort2(array))
