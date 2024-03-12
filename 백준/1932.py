N = int(input())

num = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = num[0][0]

for i in range(1, N):
    for j in range(i+1):
        if j == 0: left = 0
        else: left = dp[i-1][j-1]
        if j == i: right = 0
        else: right = dp[i-1][j]

        dp[i][j] = max(left, right) + num[i][j]

print(max(dp[N-1]))


