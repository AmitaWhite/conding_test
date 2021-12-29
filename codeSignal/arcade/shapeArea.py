from time import time

st=time()

def shapeArea(n):
    a=1

    if n==1:
        return a

    for i in range(n):
        a= a+4*(i)

    return a

for i in range(100):
    print(shapeArea(i+1))

et=time()

print(et-st)
