'''
#TestCase : Test를 위한 코드 입니다.
a = 'abdc'
b = 'addac'
a = list(a)
b = list(b)

count = 0

b.sort()
a.sort()

for i in a:
    if i in b:
        b.remove(i)
        count += 1
print(count)
print(b)
'''

def solution(s1, s2):
    s1 = list(s1)
    s2 = list(s2)

    count = 0

    s1.sort()
    s2.sort()

    for i in s1:
        if i in s2:
            s2.remove(i)
            count += 1

    return count
