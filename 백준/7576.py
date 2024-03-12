from collections import deque
def BFS():
    q = deque()
    for i, j in start:
        visited[i][j] = 1
        q.append([i, j])
    while q:
        v = q.popleft()
        x, y = v[0], v[1]
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<M and 0<=ny<N and tomato[nx][ny] != -1:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    tomato[nx][ny] = tomato[x][y]+1
                    q.append([nx, ny])


N, M = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(M)]

start = []
visited = [[0] * N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if tomato[i][j] == 1:
            start.append([i, j])

BFS()
result = 0
for k in range(M):
    if tomato[k].count(0) >= 1:
        result = -1
        break

    result = max(result, max(tomato[k])-1)


print(result)





