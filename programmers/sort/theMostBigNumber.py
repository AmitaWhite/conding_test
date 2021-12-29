'''
## TODO: 1차원 배열을 2중 배열로 만들어 풀어보기

a = [6,10,2]
b = []

for j in range(len(a)):
    c = str(a[j])
    for i in range(len(c)):
        b.append(c[i])

print(b)
'''

'''
def re(num):
    num = num.remove(num[0])

    if len(num) == 1:
        retur
'''
a = [6,10,2]

for i in range(len(a)):
    a[i] = str(a[i]) * 4

print(a)
