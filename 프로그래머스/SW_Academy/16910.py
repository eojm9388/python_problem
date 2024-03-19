T = int(input())

for tc in range(1, T+1):
    # 반지름 N
    N = int(input())
    # 반지름 N인 원안의 격자점 개수
    cnt = 0
    # x y축에 있는 격자점 개수
    cnt += 1 + N * 4
    # 1사분면의 격자점 개수 * 4 -> 대칭이기 때문에
    for i in range(1, N):
        for j in range(1, N):
            if i**2 + j**2 <= N**2:
                cnt += 4

    print(f'#{tc}', cnt)
