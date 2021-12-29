def solution(name):
    answer = 0
    min_move = len(name)-1
    move = 0
    for idx, char in enumerate(name):
        answer += min(ord(char)-ord('A'),ord('Z')-ord(char)+1 )
        move = idx + 1
        #if there is no A in name : move has len(name) - 1
        while move < len(name) and name[move] == 'A':
            move += 1
        #if there has no 'A' in name , always bigger than param1
        min_move = min(min_move, idx + idx + len(name) - move)

    answer += min_move

    return answer

print(solution("JAZ"))
