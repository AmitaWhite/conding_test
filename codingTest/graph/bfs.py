from collections import deque

def bfs(graph,start,visited):

    #queue 셍성 후, start 에 해당하는 값 하나 집어 넣음
    queue = deque([start])
    visited[start] = True

    #이후 queue 가 빌 때까지 실행 할 것임 . 현재는 queue가 start로 하나 차 있음
    #추가로 stack 을 이용 해 dfs 를 구현 해 볼 수 있음 이 때, push() , pop() 으로
    while queue:
        #start에 해당하는 값 하나를 받아 옴
        v = queue.popleft()
        print(v)

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [[],
[2,3,8],
[1,7],
[1,4,5],
[3,5],
[3,4],
[7],
[2,6,8],
[1,7]
]

visited = [False] * 9

bfs(graph,1,visited)
