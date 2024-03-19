N, M, C = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]



def A(i, j, c):
    result = []
    if j + M <= N:
        temp = MAP[i][j:j+M]
        used = [0] * M

        for k in range(M):
            if used[k] == 0:

        print(temp)




for i in range(N):
    for j in range(N):
        visited = [[0] * N for _ in range(N)]
        A(i, j, C)
