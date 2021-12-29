def solution(citations):
    citations = sorted(citations,reverse=True)

    for i in range(len(citations)):
        if citations[i] <= i :
            return i

    return len(citations)

testcase =[3,2,5,2,2,6]
print(solution(testcase))
