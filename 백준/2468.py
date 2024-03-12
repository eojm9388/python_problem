from collections import deque
N = int(input())

def BFS(i, j):
    q = deque()
    q.append([i, j])
    visited[i][j] = 1

    while q:
        v = q.popleft()
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni = v[0] + di
            nj = v[1] + dj

            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 and MAP[ni][nj] > n:
                visited[ni][nj] = 1
                q.append([ni, nj])



MAP = [list(map(int, input().split())) for _ in range(N)]
max_height = 0
for x in range(N):
    temp = max(MAP[x])
    if max_height < temp:
        max_height = temp

max_cnt = 0

for n in range(0, max_height):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if MAP[i][j] > n and visited[i][j] == 0:
                cnt += 1
                BFS(i, j)

    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)