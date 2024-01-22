K, N, M = map(int, input().split())

price = K * N
result = 0

if price > M:
    result = price - M

print(result)