a = [1,2,3,44]
for i in range(len(a)):
    b = a[i]
    a[i] = str(a[i]) * 4
    a[i] = (b,int(a[i][0:4]))

a.sort(reverse=True,key = lambda k : k[1])
print(a[0][1])
l = ''
for i in range(len(a)):
    l = l + str(a[i][0])
print(a)
print(l)


#unpacking 과 zip, join을 이용해서 풀기

c = [1,212,33,441]
d = [(c[i],(str(c[i])*4)[:4]) for i in range(len(c))]
print(d)
d.sort(reverse=True, key = lambda j : j[1])


print("answer is :",''.join(map(str,zip(*d)[0])))
