# 블록의 가로, 세로 길이
W, H = map(int, input().split())
# 상점의 개수
N = int(input())
# 최단 거리 합
result = 0
# 상점 리스트
store = []

for n in range(N):
    store.append(list(map(int, input().split())))

# 동근이의 방향과 거리
dong_direction, dong_distance = map(int, input().split())
# 상점의 방향과 거리
for store_direction, store_distance in store:
    # 동근이가 북쪽에 있을 경우
    if dong_direction == 1:
        # 상점이 북쪽일 경우 = 같은 방향
        if store_direction == 1:
            result += abs(dong_distance-store_distance)
        # 상점이 남쪽일 경우 = 반대편 방향
        elif store_direction == 2:
            # 시계, 반시계 중 더 작은 값을 골라야함
            if dong_distance + store_distance < 2 * W - (dong_distance + store_distance):
                result += dong_distance + store_distance
            else:
                result += 2 * W - (dong_distance + store_distance)
            # 높이만큼은 무조건 이동한다.
            result += H
        # 상점이 서쪽일 경우 = 반시계방향 이동
        elif store_direction == 3:
            result += store_distance + dong_distance
        # 상점이 동쪽일 경우 = 시계방향 이동
        elif store_direction == 4:
            result += W - dong_distance + store_distance
    # 동근이가 남쪽에 있을 경우
    elif dong_direction == 2:
        # 상점이 북쪽일 경우 = 반대편 방향
        if store_direction == 1:
            result += H
            if dong_distance + store_distance < 2 * W - (dong_distance + store_distance):
                result += dong_distance + store_distance
            else:
                result += 2 * W - (dong_distance + store_distance)
        # 상점이 남쪽일 경우 = 같은 방향
        elif store_direction == 2:
            result += abs(dong_distance - store_distance)
        # 상점이 서쪽일 경우 = 시계방향 이동
        elif store_direction == 3:
            result += dong_distance + H - store_distance
        # 상점이 동쪽일 경우 = 반시계방향 이동
        elif store_direction == 4:
            result += W - dong_distance + H - store_distance

    elif dong_direction == 3:
        # 상점이 북쪽일 경우 = 시계 방향
        if store_direction == 1:
            result += dong_distance + store_distance
        # 상점이 남쪽일 경우 = 반시계 방향
        elif store_direction == 2:
            result += H - dong_distance + store_distance
        # 상점이 서쪽일 경우 = 같은 방향
        elif store_direction == 3:
            result += abs(dong_distance - store_distance)
        # 상점이 동쪽일 경우 = 반대편 방향
        elif store_direction == 4:
            result += W
            if dong_distance + store_distance < 2 * H - (dong_distance + store_distance):
                result += dong_distance + store_distance
            else:
                result += 2 * H - (dong_distance + store_distance)

    elif dong_direction == 4:
        # 상점이 북쪽일 경우 = 반시계 방향
        if store_direction == 1:
            result += dong_distance + W - store_distance
        # 상점이 남쪽일 경우 = 시계 방향
        elif store_direction == 2:
            result += H - dong_distance + W - store_distance
        # 상점이 서쪽일 경우 = 반대편 방향
        elif store_direction == 3:
            result += W
            if dong_distance + store_distance < 2 * H - (dong_distance + store_distance):
                result += dong_distance + store_distance
            else:
                result += 2 * H - (dong_distance + store_distance)
        # 상점이 동쪽일 경우 = 같은 방향
        elif store_direction == 4:
            result += abs(dong_distance - store_distance)

print(result)