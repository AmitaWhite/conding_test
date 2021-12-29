'''
두 개의 배열을 입력 받아 a배열의 합이 최대가 되도록
b배열의 원소와 교체한 뒤 최댓 값 출력
'''
#greedy 수행
#n개의 원소, k번의 교체
n , k = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

#a는 오름차순
a.sort()
#b는 내림차순
b.sort(reverse = True)

for i in range(k):
    if a[i] < b[i]:
        a[i] , b[i] = b[i] , a[i]
    else:
        break #a의 원소가 b의 내림차순 원소보다 크면 바꿀 필요가 없음

print(sum(a))
