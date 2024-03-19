# import sys
# sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 화폐 단위: 개수
    money = {
        50000: 0,
        10000: 0,
        5000: 0,
        1000: 0,
        500: 0,
        100: 0,
        50: 0,
        10: 0
    }
    # 거스름돈
    N = int(input())
    # 큰 금액부터 개수를 구한여 딕셔너리의 값에 더한다
    # 현재 금액의 개수 -> 거스름돈 // 현재 금액
    # 가스름돈 % 현재 금액 -> 다음 화폐를 구할 때 쓸 거스름돈
    for coin in money:
        money[coin] = N // coin
        N %= coin
    # 순서대로 출력한다
    print(f'#{tc}')
    for i in money:
        print(money[i], end=' ')

    print()