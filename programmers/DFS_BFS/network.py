from collections import deque

#que에 방문할 노드를 쌓고, 방문한 노드를 표시함
#방문했다면 que에서 추출함으로써 bfs 수행
def bfs(x,y,computers,node_num):
    que = deque()
    que.append((x,y))
    visited = set()

    #que 가 완전히 비워지면 모든 순회를 끝냄
    while que:
        #dfs에 압력값 x,y가 state, connected로 표현됨
        state, connected = que.popleft()
        #connected 값을 방문 처리
        visited.add(connected)

        for i in range(node_num):
            #computers 내에서 connected와 i번째 노드가 연결 돼 있으면
            if computers[connected][i] == 1:
                #i번째 노드를 방문하지 않았다면
                if i not in visited:
                    que.append((connected,i))
                computers[connected][i] = 0


def solution(n, computers):
    answer = 0

    for i in range(len(computers)):
        for j in range(len(computers[0])):
            #i,j가 연결 되어 있다면
            if computers[i][j] == 1:
                dfs(i,j,computers,n)
                answer += 1
    return answer


testCase = [[1,1,0],[1,1,0],[0,0,1]]
t2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(3,t2))
