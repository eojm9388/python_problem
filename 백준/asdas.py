def backtracking(cnt, i, b):
    global result

    if cnt >= result:       # 가지치기
        return

    if i == (n-2) and b > 0:       # 도달하면 result = cnt
        result = cnt
        return

    elif b > 0 and 0 <= i < n-2:
        backtracking(cnt+1, i+1, battery[i+1])    # 충전 할 경우
        backtracking(cnt, i+1, b-1)  # 충전 안 할 경우

    else:
        return

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    battery = list(map(int, input().split()))
    n = battery.pop(0)
    result = float('inf')

    backtracking(0, 0, battery[0])
    print(result)