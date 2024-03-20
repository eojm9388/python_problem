import sys
input = sys.stdin.readline

N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

# 누적합 구하기
sum_MAP = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        sum_MAP[i][j] = sum_MAP[i][j-1] + sum_MAP[i-1][j] - sum_MAP[i-1][j-1] + MAP[i-1][j-1]


for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    print(sum_MAP[x2][y2] - sum_MAP[x1-1][y2] - sum_MAP[x2][y1-1] + sum_MAP[x1-1][y1-1])