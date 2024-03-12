N = int(input())

arr = [int(input()) for _ in range(N)]

dp = [0] * N

if N <= 2:
    print(sum(arr))

else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0], arr[1]) + arr[2]

    for i in range(3, N):
        dp[i] = dp[i-3] + arr[i-1] + arr[i]

        dp[i] = max(dp[i], dp[i-2] + arr[i])


    print(dp[N-1])

