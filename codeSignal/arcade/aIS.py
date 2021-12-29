count = 0
a = [1,2,1,2]

for i in range(len(a) - 1):
    if a[i] > a[i + 1]:
        count = count + 1


if count < 2 :
    print("True")

else:
    print("False")
