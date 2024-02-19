# import sys
# sys.stdin = open('input.txt')

from collections import deque
# 5105 미로의 거리 문제와 동일
# 상하좌우 델타 탐색
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# BFS함수 생성
def BFS(S, G):
    q = deque()
    i, j = S[0], S[1]
    visited[i][j] = 1
    q.append((i, j))

    while q:
        now = q.popleft()
        i, j = now[0], now[1]
        for n in range(4):
            ni = i + di[n]
            nj = j + dj[n]

            if 0<=ni<16 and 0<=nj<16:
                if miro[ni][nj] == 3:
                    return 1
                elif visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni, nj))

    return 0


for t in range(1, 11):
    tc = int(input())
    miro = [list(map(int, input())) for _ in range(16)]
    visited = [miro[k][:] for k in range(16)]

    S = (1, 1)
    G = (13, 13)
    print(f'#{tc}', BFS(S, G))
    # for _ in range(16):
    #     print(miro[_])