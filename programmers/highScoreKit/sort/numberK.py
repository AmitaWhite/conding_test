#Test Case
'''
answer = []
divide = []

array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]

divide = array[commands[0][0]-1:commands[0][1]]
print(divide)
print(divide[commands[0][2]-1])


for i in range(len(commands)):
    divide = array[commands[i][0]-1:commands[i][1]]
    divide.sort()
    answer.append(divide[commands[i][2]-1])

print(answer)
'''

#solution
def solution(array, commands):
    answer = []
    divide = []

    for i in range(len(commands)):
        #2차원 배열에서 원소 값을 참조하여 배열을 자릅니다.
        divide = array[commands[i][0]-1:commands[i][1]]
        divide.sort()
        answer.append(divide[commands[i][2]-1])
    return answer
