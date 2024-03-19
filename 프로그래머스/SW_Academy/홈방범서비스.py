T = int(input())

# 해당 좌표에 손해를 보지 않는 가장 많은 집의 개수를 구해주는 함수
def f(i, j):
    global max_cnt
    K = 1
    result = 0
    # 도시 전체에 서비스 될때 최악의 경우 K = N + (N-1)
    while K <= N + (N-1):
        # 서비스 운영 비용
        cost = K * K + ((K - 1) * (K - 1))
        # 주민들이 내는 비용
        money = 0
        # 집 개수
        cnt = 0
        # 서비스 지역 내에 집이 있으면 집 추가 및 주민 비용 추가
        for x, y in house_p:
            distance = abs(x - i) + abs(y - j)
            if distance <= (K - 1):
                money += M
                cnt += 1
        # 손해를 보지 않는다면 집 개수 갱신
        if cost <= money:
            result = cnt
        K += 1
    # while문이 끝나면 result에는 현재 위치 좌표에서
    # 구할 수 있는 집의 개수의 최댓값이 들어있다

    # 최댓값 갱신
    if max_cnt < result:
        max_cnt = result





for tc in range(1, T+1):
    # 도시의 크기 N, 하나의 집이 지불할 수 있는 금액 M
    N, M = map(int, input().split())

    # 도시
    MAP = [list(map(int, input().split())) for _ in range(N)]
    # 집들의 위치
    house_p = []
    # 집들의 위치좌표를 구해준다
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 1:
                house_p.append([i, j])
    # 손해를 보지 않는 가장 많은 집의 개수
    max_cnt = 0
    # 완전 탐색
    for i in range(N):
        for j in range(N):
            f(i, j)



    print(f'#{tc}', max_cnt)

