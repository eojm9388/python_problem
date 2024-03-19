# 배낭의 무게 W, 금속의 종류 N
W, N = map(int, input().split())

# 금속 정보
metal = [list(map(int, input().split())) for _ in range(N)]

# 금속의 무게당 가격순으로 정렬
metal.sort(key=lambda x:x[1])
# 배낭에 담은 금속의 가격
cost = 0
# 배낭에 담을 수 있을 때까지
while W > 0:
    # metal에 마지막 원소가 무게당 가격이 제일 높다
    high_metal = metal.pop()
    # 만약 금속을 다 담을 수 있다면
    if W > high_metal[0]:
        # 배낭 무게 감소
        W -= high_metal[0]
        # 금액 추가
        cost += high_metal[1] * high_metal[0]

    # 금속의 일정양만 담을 수 있다면
    else:
        # 남은 배낭 무게만큼 담기
        cost += high_metal[1] * W
        W = 0

print(cost)