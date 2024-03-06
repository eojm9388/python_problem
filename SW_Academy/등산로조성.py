T = int(input())

def go_trip(i, j, n, k):
    if k < 0:
        result.append(n-1)
        return
    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ni = i + di
        nj = j + dj

        if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
            if MAP[ni][nj] < MAP[i][j]:
                visited[ni][nj] = 1
                go_trip(ni, nj, n+1, k)
                visited[ni][nj] = 0
            elif MAP[ni][nj] - K < MAP[i][j] and k == 1:
                temp = abs(MAP[i][j] - MAP[ni][nj]) + 1
                visited[ni][nj] = 1
                MAP[ni][nj] -= temp
                go_trip(ni, nj, n+1, k-1)
                visited[ni][nj] = 0
                MAP[ni][nj] += temp

    result.append(n)



for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    MAP = [list(map(int, input().split())) for _ in range(N)]

    high_p = []
    visited = [[0] * N for _ in range(N)]

    max_num = 0

    for _ in range(N):
        num = max(MAP[_])
        if max_num < num:
            max_num = num

    for i in range(N):
        for j in range(N):
            if MAP[i][j] == max_num:
                high_p.append([i, j])

    result = []
    for x, y in high_p:
        visited[x][y] = 1
        go_trip(x, y, 1, 1)
        visited[x][y] = 0
    # print(result)
    print(f'#{test_case}', max(result))
