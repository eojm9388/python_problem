N, K = map(int, input().split())

coin = [int(input()) for _ in range(N)]

cnt = 0
while K > 0:
    current_coin = coin.pop()
    cnt += K // current_coin
    K %= current_coin

print(cnt)
