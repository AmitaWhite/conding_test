n , m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))


#DFS 로 특정한 노드를 방문한 뒤에 연결된 모든 노드들을 방문
def dfs(x,y):
    #주어진 범위를 벗어 나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    #현재 노드를 아직 방문 하지 않았다면
    if graph[x][y] == 0:
        #현재 노드를 방문 처리
        graph[x][y] = 1
        #상,하,좌,우 위치에도 재귀적 호출
        #상하좌우에서 또한 연결된 모든 노드를 재귀적 방문
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)

        #이후 방문한 모든 노드를 1 로 처리한 뒤 True 를 리턴
        #각 True 값의 합이 반환 해야 할 결과가 됨
        return True

    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count = count + 1

print(count)
