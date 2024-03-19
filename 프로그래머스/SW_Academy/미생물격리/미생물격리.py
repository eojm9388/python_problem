import sys
sys.stdin = open("input.txt")

T = int(input())

di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

def total():
    for i in range(N):
        for j in range(N):
            if MAP[i][j] != 0:
                MAP[i][j].sort(key=lambda x:x[2])

                x, y = MAP[i][j][-1][0], MAP[i][j][-1][1]
                d = MAP[i][j][-1][3]
                cnt = 0
                for mi in MAP[i][j]:
                    cnt += mi[2]

                temp.append([x, y, cnt, d])


def total_cnt():
    result = 0
    for t in temp:
        result += t[2]

    return result


for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(K)]
    temp = arr
    for m in range(M):
        MAP = [[0] * N for _ in range(N)]
        K = len(temp)
        for n in range(K):
            i, j, cnt, d = temp[n]

            ni = i + di[d]
            nj = j + dj[d]

            if ni == 0 or ni == N-1 or nj == 0 or nj == N-1:
                if d == 1:
                    d = 2
                elif d == 2:
                    d = 1
                elif d == 3:
                    d = 4
                elif d == 4:
                    d = 3

                cnt //= 2


            if MAP[ni][nj] == 0:
                MAP[ni][nj] = [[ni, nj, cnt, d]]
            else:
                MAP[ni][nj].append([ni, nj, cnt, d])

        temp = []
        total()

    print(f'#{tc}', total_cnt())