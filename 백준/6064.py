T = int(input())

for tc in range(T):
    M, N, x, y = map(int, input().split())

    cnt = x
    y_1 = x
    while y_1 != y:
        y_1 += M
        if y_1 > N:
            y_1 %= N

        cnt += M
        if y_1 == x:
            cnt = -1
            break

    print(cnt)