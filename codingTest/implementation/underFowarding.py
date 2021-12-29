n = int(input())

array =[]
for _ in range(n):
    array.append(list(map(int,input())))


def underFowarding(n,array):
    result = sorted(array,reverse = True)

    return result


print(underFowarding(n,array))
