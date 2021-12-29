# a = [-1,150,160,-1,-1,168,-1,120]
# print(a)
# l = sorted([i for i in a if i>0])
# print(l)
#
# for idx, value in enumerate(a):
#     if value == -1:
#         l.insert(idx, value)
#         print(l)
#
# print(l)

a = [1,3,5,7]
b = [2,4,6,8]

for idx, value in enumerate(a):
    b.insert(idx*2,value)

print(b)
