N = int(input())

time = [list(map(int, input().split())) for _ in range(N)]
time.sort()
# print(time)

cnt = 1
start, end = time[0][0], time[0][1]

for s, e in time[1:]:
    if s >= end:
        cnt += 1
        end = e

    elif e < end:
        end = e



print(cnt)
