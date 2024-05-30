from collections import deque
N, M = map(int, input().split())

MAP = [list(map(int, list(input()))) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

q = deque()
q.append([0, 0])
visited[0][0] = 1

while q:
    i, j = q.popleft()
    # print(i, j)
    if i == N-1 and j == M-1:
        break


    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ni = i + di
        nj = j + dj

        if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0 and MAP[ni][nj] == 1:
            visited[ni][nj] = visited[i][j] + 1
            q.append([ni, nj])


print(visited[N-1][M-1])