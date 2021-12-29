from time import time

st=time()

def shapeArea(n):

    result = 1
    if n==1:
        return result
    else:
        result= result+ 2*((n-1)**2)+ 2*(n-1)
        return result


for i in range(100):
    shapeArea(i)

et=time()

print(et-st)
