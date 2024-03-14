N = int(input())
wait_time = list(map(int, input().split()))

wait_time.sort()

result = 0
for i in range(N):
    for j in range(i+1):
        result += wait_time[j]


print(result)
