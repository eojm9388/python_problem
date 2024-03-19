T = int(input())

# 좌표값 i, j, 경로 합 s
def f(i, j, s):
    global min_total
    # 경로 합이 이미 최소값을 넘어간 경우
    # 그 경로는 탈락
    if s > min_total:
        return
    # 마지막 목적지까지 도달했다면 경로 합이 최소이다
    if i == N-1 and j == N-1:
        min_total = s

    # 아래, 왼쪽으로 이동
    for di, dj in [[1, 0], [0, 1]]:
        ni = i + di
        nj = j + dj
        # 범위안에 있다면 이동 시킨다
        if ni < N and nj < N:
            f(ni, nj, s+MAP[ni][nj])


for tc in range(1, T+1):
    N = int(input())

    MAP = [list(map(int, input().split())) for _ in range(N)]
    # 초기 최소합
    min_total = 13 * 13 * 11
    # 무조건 (0, 0)에서 출발 
    f(0, 0, MAP[0][0])

    print(f'#{tc}', min_total)



