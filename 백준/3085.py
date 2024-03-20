def search_row(i, j):
    global max_cnt
    color = MAP[i][j]
    chance = 1
    cnt = 0
    while j < N:
        if MAP[i][j] == color:
            cnt += 1
        else:
            if i+1 < N and MAP[i+1][j] == color and chance:
                cnt += 1
                chance -= 1
            elif i-1 >= 0 and MAP[i-1][j] == color and chance:
                cnt += 1
                chance -= 1
            elif j+1 < N and MAP[i][j+1] == color and chance:
                cnt += 1
                if max_cnt < cnt:
                    max_cnt = cnt
                    break
            else:
                if max_cnt < cnt:
                    max_cnt = cnt
                    break
        j += 1
    if max_cnt < cnt:
        max_cnt = cnt

def search_column(i, j):
    global max_cnt
    color = MAP_T[i][j]
    chance = 1
    cnt = 0
    while j < N:
        if MAP_T[i][j] == color:
            cnt += 1
        else:
            if i+1 < N and MAP_T[i+1][j] == color and chance:
                cnt += 1
                chance -= 1
            elif i-1 >= 0 and MAP_T[i-1][j] == color and chance:
                cnt += 1
                chance -= 1
            elif j+1 < N and MAP_T[i][j+1] == color and chance:
                cnt += 1
                if max_cnt < cnt:
                    max_cnt = cnt
                break
            else:
                if max_cnt < cnt:
                    max_cnt = cnt
                break
        j += 1
    if max_cnt < cnt:
        max_cnt = cnt

N = int(input())

MAP = [list(input()) for _ in range(N)]
MAP_T = [[MAP[y][x] for y in range(N)] for x in range(N)]
max_cnt = 0
for i in range(N):
    for j in range(N):
        search_row(i, j)
        search_column(i, j)


print(max_cnt)




