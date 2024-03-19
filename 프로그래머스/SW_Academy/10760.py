T = int(input())

def search(i, j):
    global result
    # 현재 높이보다 낮은 지점 개수
    cnt = 0
    # 8방향 델타 탐색
    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
        ni = i + di
        nj = j + dj
        # 범위 안이라면
        if 0<=ni<N and 0<=nj<M:
            # 높이가 낮으면
            if MAP[ni][nj] < MAP[i][j]:
                # 개수 증가
                cnt += 1
                # 개수가 4개 이상이라면 예비 후보지 추가
                if cnt >= 4:
                    result += 1
                    return


for tc in range(1, T+1):
    # 구역의 크기
    N, M = map(int, input().split())
    # 예비 후보지 개수
    result = 0
    # 착륙지 높이 2차원 리스트
    MAP = [list(map(int, input().split())) for _ in range(N)]
    # 완전 탐색
    for i in range(N):
        for j in range(M):
            search(i, j)

    print(f'#{tc}', result)