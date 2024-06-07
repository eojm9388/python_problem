N = int(input())

arr = list(map(int, input().split()))

max_cnt = 0

for i in range(2, 100):
    cnt = 0
    for j in arr:
        if j % i == 0:
            cnt += 1

    max_cnt = max(max_cnt, cnt)

print(max_cnt)