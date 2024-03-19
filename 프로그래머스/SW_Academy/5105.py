# import sys
# sys.stdin = open('input.txt')
# 큐를 생성하기 위한 라이브러리
from collections import deque

T = int(input())

# 상하좌우 델타 탐색
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
# BFS 함수 생성 (시작점:S, 끝점:G)
def BFS(S, G):
    # 큐 생성
    q = deque()
    # 시작점의 i, j 좌표
    i, j = S[0], S[1]
    # 시작점의 좌표 방문 처리
    visited[i][j] = 1
    # 시작점 enqueue
    q.append((i, j))
    # q가 빌때까지
    while q:
        # 현재 좌표
        now = q.popleft()
        # 현재 좌표를 상하좌우로 델타 탐색한다.
        for k in range(4):
            ni = now[0] + di[k]
            nj = now[1] + dj[k]
            # 미로의 범위안에 있어야한다.
            if 0<=ni<N and 0<=nj<N:
                # 만약 상하좌우중 도착지점이 있다면
                if ni == G[0] and nj == G[1]:
                    # 그 전에 있던 노드의 이동거리-1 -> 시작지점을 거리 1로 두었기 때문에
                    return visited[now[0]][now[1]] - 1
                # 도착지점이 아니고 벽이 아닐 경우
                elif visited[ni][nj] == 0:
                    # 이동거리 1 증가 후 방문처리
                    visited[ni][nj] = visited[now[0]][now[1]] + 1
                    # 큐에 좌표 추가
                    q.append((ni, nj))
    # 모두를 탐색해도 도착지점을 못 찾았다면
    # 0 반환
    return 0


for tc in range(1, T+1):
    # 미로의 크기
    N = int(input())
    # 미로 2차원 리스트
    miro = [list(map(int, input())) for _ in range(N)]
    # 방문 처리를 해줄 2차원 리스트
    visited = [[0]*N for _ in range(N)]
    # 시작지점과 도착지점을 찾고 벽을 방문 처리 해준다.
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                S = (i, j)
            elif miro[i][j] == 3:
                G = (i, j)
            elif miro[i][j] == 1:
                visited[i][j] = 1
    # print(S, G)
    print(f'#{tc}', BFS(S, G))
    # for _ in range(N):
    #     print(visited[_])

