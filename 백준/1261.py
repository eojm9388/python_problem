from collections import deque

def BFS():
    global min_cnt
    q = deque()
    q.append([0, 0, 0])

    while q:
        v = q.popleft()

        if v[2] > min_cnt:
            continue
        if [v[0], v[1]] == [M-1, N-1]:
            if min_cnt > v[2]:
                min_cnt = v[2]

        i, j = v[0], v[1]

        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0<=ni<M and 0<=nj<N and ni == nj != 0:
                q.append([ni, nj])
                if miro[ni][nj] == 1:
                    if visited[ni][nj] > visited[i][j] + 1:
                        visited[ni][nj] = visited[i][j] + 1
                else:
                    if visited[ni][nj] > visited[i][j]:
                        visited[ni][nj] = visited[i][j]


N, M = map(int, input().split())

miro = [list(map(int, list(input()))) for _ in range(M)]

visited = [[0]*N for _ in range(M)]
min_cnt = max((M-1) + (N-2), 0)

visited[0][0] = 1
BFS()
print(min_cnt)
