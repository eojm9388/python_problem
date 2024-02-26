T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 전선이 연결된 전봇대 높이
    bong = [list(map(int, input().split())) for _ in range(N)]
    # 교차점 개수
    cnt = 0
    # 밑에서부터 개수를 셀 것이기 때문에 정렬 필요
    bong.sort()

    for i in range(N):
        for j in range(1, N):
            # 밑에 줄
            a_i, a_j = bong[i]
            # 위에 줄
            b_i, b_j = bong[j]
            # 밑에 줄과 위에 줄이 교차 되었는지 확인
            if a_i < b_i and a_j > b_j:
                cnt += 1

    print(f'#{tc}', cnt)

