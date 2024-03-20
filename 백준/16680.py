from collections import deque
N, K = map(int, input().split())


di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]

MAP = [[0] + list(map(int, input().split())) for _ in range(N)] + [[0] * (N+1)]
chess = deque([list(map(int, input().split())) for _ in range(K)])

print(chess)
visited = [[[] for _ in range(N)] for _ in range(N)]


while chess:
    v = chess.popleft()
    i, j, d = v[0], v[1], v[2]

    ni = i + di[d]
    nj = j + dj[d]

    if 0<=ni<N and 0<=nj<N:
        if MAP[ni][nj] == 0:
            if visited[ni][nj] == []:
                chess.append([ni, nj, d])
            visited[ni][nj].append([ni, nj, d])

        if MAP[ni][nj] == 1:
            if visited[ni][nj] == []:
                chess.append([ni, nj, d])

            else:
                visited[ni][nj].reverse()
                chess.append(visited[ni][nj][0])




print(visited)


