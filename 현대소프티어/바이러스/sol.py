K, P, N = map(int,input().split())

for i in range(N):
    K = (P*K) % 1000000007

print(K)
