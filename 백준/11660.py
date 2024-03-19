import sys
N, M = map(int, sys.stdin.readline().split())

MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    temp = 0
    for j in range(1, N+1):
        temp += MAP[i-1][j-1]

        dp[i][j] = temp

for k in range(M):
    temp = list(map(int, input().split()))
    result = 0
    x1, y1, x2, y2 = temp[0],temp[1],temp[2],temp[3]

    for i in range(x1, x2+1):
        result += dp[i][y2]
        result -= dp[i][y1-1]

    print(result)



