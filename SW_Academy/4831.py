import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def go_trip(start, K, end):           # 전기버스가 이동할 수 있는지 판단하고
                                      # 한번 이동할 때 거리를 반환해줄 함수
    available = False                 # 전기차가 이동 못한다고 가정
    if start + K >= end:              # 만약 도착점에 도착했다면 이동 가능과 도착지점을 반환
        available = True
        return available, end

    # 도착지점을 가지 못한 경우
    # 출발점 다음부터 이동거리까지 충전소가 있는지 확인
    partial_range = charging_station[start+1:start+K+1]
    counts = partial_range.count(1)

    # 만약 충전소가 있다면
    if counts >= 1:
        # 이동 가능
        available = True
        # 2개 이상이라면 최대한 뒤에 충전소에서 충전하는 것이
        # 최소 충전소를 거쳐 가는거임
        partial_range.reverse()
        # 이동한 후에 전기버스의 위치
        charging_position = start + K - partial_range.index(1)
        # 이동 가능과 이동후 전기버스의 위치를 반환
        return available, charging_position
    else:
        # 충전소가 없다면 이동 불가능과 0을 반환
        return available, 0






for test_case in range(1, T + 1):
    charging_count = 0
    K, N, M = map(int, input().split())
    charging_station_position = list(map(int, input().split()))
    # 충전소의 위치를 인덱스로 받기 위한 리스트 생성
    charging_station = [0] * (N+1)
    # 충전소의 위치 할당
    for position in charging_station_position:
        charging_station[position] = 1

    count = 0                # 충전횟수
    start = 0                # 시작지점
    x, y = go_trip(start, K, N)  # 시작지점부터 출발 x: 이동가능여부, y: 이동한 거리
    while True:
        if not x:            # 이동 불가능이라면 이동횟수를 0으로 바꾸고 반복문 탈출
            count = 0
            break
        elif y == N:         # 도착지점에 도착했다면 반복문 탈출
            break
        elif x:
            count += 1       # 이동가능하고 도착지점에 도착하지 않으면 충전횟수 증가
        x, y = go_trip(y, K, N) # 다시 이동

    print(f'#{test_case}', count)


