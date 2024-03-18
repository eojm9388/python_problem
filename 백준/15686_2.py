from itertools import combinations

N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken_house = []

min_dis = 99999999

# 집들과 치킨집의 좌표 구하기
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1:
            house.append([i, j])
        elif MAP[i][j] == 2:
            chicken_house.append([i, j])

# 치킨집들 중에서 M개를 무작위로 골라 거리 계산
for chicken in combinations(chicken_house, M):
    result = 0
    for i, j in house:
        chicken_len = 999
        # 치킨집들 중 거리가 제일 낮은 곶 계산
        for x, y in chicken:
            chicken_len = min(abs(x-i)+abs(y-j), chicken_len)
        # 무작위로 치킨집을 골랐을 때 치킨 거리
        result += chicken_len
    # 최소 치킨 거리 구하기
    min_dis = min(min_dis, result)

print(min_dis)