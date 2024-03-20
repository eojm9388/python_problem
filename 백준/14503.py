N, M = map(int, input().split())
# 로봇 청소기 위치, 방향
r, c, d = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

# 방향에 따른 델타 탐색
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
# 방문처리 = 청소를 한 곳 + 벽
visited = [[0] * M for _ in range(N)]
# 청소한 구역 개수
n = 0

# MAP내의 벽 방문처리
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1:
            visited[i][j] = 1

i, j = r, c
# 행동 2에서 후진 했을 때 벽이라면 로봇 작동 멈춤
# 그 전까지는 반복
while True:
    # 행동 1
    # 현재 칸이 청소하지 않은 곳이라면 청소
    if visited[i][j] == 0:
        visited[i][j] = 1
        # 청소 구역 + 1
        n += 1
    # 현재 칸의 주변 4곳 탐색
    for temp_i, temp_j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        temp_ni = i + temp_i
        temp_nj = j + temp_j
        # 3번 행동
        # 4칸 중 청소하지 않은 빈 칸이 있을 경우
        if visited[temp_ni][temp_nj] == 0:
            # 90도 회전
            d = (d-1) % 4
            # 만약 앞칸이 청소하지 않은 곳이라면 이동
            if visited[i+di[d]][j+dj[d]] == 0:
                i += di[d]
                j += dj[d]
                # 1번 행동으로 돌아감
                break
            # 청소한 곳이라면 그냥 1번으로 돌아감
            else:
                break
    # 2번 행동
    # 위의 4곳을 탐색하는 for문을 모두 통과했다면 주변에 청소할 곳이 없는 것
    else:
        # 만약 후진을 했는데 벽이라면 작동 멈춤
        if MAP[i-di[d]][j-dj[d]] == 1:
            break
        # 벽이 아니면 후진
        else:
            i -= di[d]
            j -= dj[d]
        # 1번으로 돌아감

print(n)
