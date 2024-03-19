from itertools import permutations

def f(x, y, i, c):
    global max_cnt
    if i == 3:
        if max_cnt < c:
            max_cnt = c
            temp_2 = path[:]
            path_result.append(temp_2)
        return

    for n in range(4):
        nx = x + dx[n]
        ny = y + dy[n]

        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            temp = temp_MAP[nx][ny]
            visited[nx][ny] = 1
            path.append([nx, ny])
            f(nx, ny, i+1, c+temp)
            visited[nx][ny] = 0
            path.pop()



N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

friends = [list(map(int, input().split())) for _ in range(M)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result_list = []

for arr in permutations(friends):
    result = 0
    temp_MAP = [MAP[x][:] for x in range(N)]
    # print(temp_MAP)
    for friend in arr:
        max_cnt = 0
        path_result = []
        path = []
        visited = [[0] * N for _ in range(N)]
        x, y = friend[0]-1, friend[1]-1
        visited[x][y] = 1
        f(x, y, 0, temp_MAP[x][y])
        temp_MAP[x][y] = 0
        for p in path_result[-1]:
            temp_MAP[p[0]][p[1]] = 0
        result += max_cnt
    result_list.append(result)

print(max(result_list))