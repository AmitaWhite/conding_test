def isLucky(n):
    a = str(n)
    a = list(a)

    for i in range(len(a)):
        a[i] = int(a[i])

    if len(a) % 2 == 0:
        frontHalf = a[ :len(a)/2]
        rearHalf = a[len(a)/2: ]

        if sum(frontHalf) == sum(rearHalf):
            return True
        else:
            return False
    else:
        return False
