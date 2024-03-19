import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # 버스 노선의 개수
    N = int(input())
    # 각 정류장의 A위치와 B위치를 담을 리스트
    A = []
    B = []
    # 각 정류장에 지나가는 버스의 대수를 담을 리스트
    result = []
    # 버스 노선에 따른 정류장 위치를 넣는다.
    for n in range(N):
        An, Bn = map(int, input().split())
        A.append(An)
        B.append(Bn)

    # 정류장 개수
    P =int(input())

    # 정류장의 위치에 버스 노선이 포함되어 있다면
    # 지나가는 버스의 수를 증가시킨다.
    for p in range(P):
        # 지나가는 버스
        bus = 0
        # 현재 정류장 위치
        Cn = int(input())
        # 현재 정류장이 각 노선 사이에 있는가
        for i in range(N):
            if A[i] <= Cn <= B[i]:
                bus += 1

        result.append(bus)

    print(f'#{test_case}', *result)


