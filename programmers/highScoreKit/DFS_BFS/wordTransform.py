from collections import deque
#1글자만 변환 가능한지 확인
def check(x,y):
    count = 0
    for i,j in zip(x,y):
        if i != j:
            count += 1
    return count == 1

def bfs(begin, target, words):
    que = deque()
    que.append((begin,0))
    visited = [False] * len(words)

    while que:
        b,depth = que.popleft()
        if b == target:
            return depth
        for i in range(len(words)):
            if check(b,words[i]):
                if visited[i] != True:
                    visited[i] = True
                    que.append((words[i],depth+1))
    return 0

b = "hit"
t = "cog"
w = ["hot", "dot", "dog", "lot", "log"]

print(bfs(b,t,w))
