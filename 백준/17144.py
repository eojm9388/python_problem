R, C, T = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]

def diffusion(i, j):
    temp = MAP[i][j] // 5
    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ni = i + di
        nj = j + dj
        if 0<=ni<R and 0<=nj<C and [ni, nj] not in robot:
            temp_MAP[ni][nj].append(temp)
            MAP[i][j] -= temp
            if [ni, nj] not in temp_arr:
                temp_arr.append([ni, nj])

def total():
    for i in range(R):
        for j in range(C):
            while temp_MAP[i][j]:
                MAP[i][j] += temp_MAP[i][j].pop()

temp_MAP = [[[] for _ in range(C)] for _ in range(R)]

# 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def air_clean():
    r1, c1 = robot[0]
    r2, c2 = robot[1]

    i, j = r1-1, c1
    d1 = 0
    while [r1, c1] != [i, j]:
        ni = i + di[d1]
        nj = j + dj[d1]

        if (ni == 0 and nj == 0) or (ni == 0 and nj == C-1) or (ni == r1 and nj == C-1) or (ni == r1 and nj == 0):
            d1 = (d1 + 1) % 4

        MAP[i][j] = MAP[ni][nj]
        i, j = ni, nj

    MAP[r1][1] = 0

    x, y = r2+1, c2
    d2 = 0
    while [r2, c2] != [x, y]:
        nx = x + dx[d2]
        ny = y + dy[d2]

        if (nx == r2 and ny == 0) or (nx == R-1 and ny == C-1) or (nx == r2 and ny == C-1) or (nx == R-1 and ny == 0):
            d2 = (d2 + 1) % 4

        MAP[x][y] = MAP[nx][ny]
        x, y = nx, ny

    MAP[r2][1] = 0


robot = []
arr = []

for i in range(R):
    for j in range(C):
        if MAP[i][j] == -1:
            robot.append([i, j])

        if MAP[i][j] > 0:
            arr.append([i, j])

for t in range(T):
    temp_arr = []
    for i, j in arr:
        diffusion(i, j)
    total()

    # for _ in range(R):
    #     print(temp_MAP[_])
    # print()
    air_clean()
    # for _ in range(R):
    #     print(MAP[_])
    # print()
    arr = temp_arr[:]

result = 0
for i in range(R):
    for j in range(C):
        if MAP[i][j] > 0:
            result += MAP[i][j]
    # print(MAP[_])

print(result)