T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 카드 정보
    card = list(input().split())
    # 카드 갯수가 홀수라면 마지막에 빈 카드를 추가하여 짝을 맞춰준다
    if N % 2 == 1:
        card += ['']
        N += 1

    # 카드 반 나누기
    card_A = card[:N//2]
    card_B = card[N//2:]

    # 하나씩 출력
    print(f'#{tc}', end=' ')
    for i in range(N//2):
        print(card_A[i], card_B[i], end=' ')

    print()


