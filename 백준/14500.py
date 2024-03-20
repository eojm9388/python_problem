N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

# 5번 블럭의 4방향의 탐색 좌표 (ㅜ, ㅗ, ㅏ, ㅓ)
plus_block_i = [[0, 0, 0, 1], [1, 1, 1, 0], [0, 1, 2, 1], [0, 1, 2, 1]]
plus_block_j = [[0, 1, 2, 1], [0, 1, 2, 1], [0, 0, 0, 1], [1, 1, 1, 0]]

# 위의 문제에서 5번 블럭을 제외하면 모든 블럭을 델타탐색으로 만들 수 있다
# f(세로위치, 가로위치, 정사각형 개수, 수들의 합)
def f(i, j, n, c):
    global max_cnt
    # 처음에 하나를 더한 상태에서 시작하기 때문에 3개가 추가되면
    # 테트로미노 완성
    if n == 3:
        max_cnt = max(max_cnt, c)
        return
	# 델타 탐색 (1~4번 블럭이 완성됨)
    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ni = i + di
        nj = j + dj

        if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            f(ni, nj, n+1, c+MAP[ni][nj])
            visited[ni][nj] = 0

# 5번 블럭에 들어가는 수를 따로 구해준다.
def plus(i, j):
    global max_cnt
    for d in range(4):
        c = 0
        for n in range(4):
            ni = i + plus_block_i[d][n]
            nj = j + plus_block_j[d][n]

            if 0 <= ni < N and 0 <= nj < M:
                c += MAP[ni][nj]

        max_cnt = max(max_cnt, c)

max_cnt = 0
visited = [[0] * M for _ in range(N)]
# 완전 탐색
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        # 1~4번 블럭 최대값
        f(i, j, 0, MAP[i][j])
        visited[i][j] = 0
        # 5번 블럭 최댓값
        plus(i, j)

print(max_cnt)