N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken_house = []
dis = []
# 치킨집과 집들 좌표 구하기
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1:
            house.append([i, j])
        elif MAP[i][j] == 2:
            chicken_house.append([i, j])

# 각 집에서 각 치킨집까지 거리 구하기
for i, j in house:
    temp = []
    for x, y in chicken_house:
        temp.append(abs(x - i) + abs(y - j))

    dis.append(temp)

min_dis = 50 * 50 * 13


# f(집 개수, 현재까지 치킨 거리, 치킨집 개수)
def f(i, k, c):
    global min_dis
    # 최소 치킨거리를 넘거나 M개보다 많은 치킨집을 고른 경우 리턴
    if k > min_dis or c > M:
        return

    # 모든 집의 치킨 거리를 구한 경우 최소 치킨 거리 갱신
    if i == P:
        if min_dis > k:
            min_dis = k
        return
    # 치킨집을 하나씩 본다
    for j in range(len(chicken_house)):
        # 만약 전에 선택한 치킨집이라면 중복 치킨집
        if used[j] == 1:
            f(i + 1, k + dis[i][j], c)
        # 만약 전에 선택한 적이 없는 치킨집이라면
        else:
            # 치킨집 개수 추가
            used[j] = 1
            f(i + 1, k + dis[i][j], c + 1)
            # 초기화
            used[j] = 0


P = len(house)

used = [0] * len(chicken_house)
# 시간 단축을 위한 코드
if M >= len(chicken_house):
    min_dis = 0
    for u in dis:
        min_dis += min(u)
else:
    f(0, 0, 0)

print(min_dis)