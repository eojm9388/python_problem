T = int(input())

for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())

    # 거리 = 시간 * 속력
    # 시간 = 거리 / 속력
    # 나눗셈은 오차를 발생시킴 -> 오차를 곱하면 오차가 더 커짐 -> 나눗셈을 맨 마지막에 하자

    distance = D * F / (A+B)

    print(f'#{tc}', distance)
