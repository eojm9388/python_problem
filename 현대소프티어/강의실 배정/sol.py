N = int(input())
room_time = [list(map(int, input().split())) for _ in range(N)]
room_time.sort()

start, end = room_time[0][0], room_time[0][1]
cnt = 1

for s, e in room_time[1:]:
    if s >= end:
        cnt += 1
        end = e
    elif e < end:
        end = e

print(cnt)