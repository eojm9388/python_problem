T = int(input())

for test_case in range(T):
    # A에 대해 입력받는 값
    A = list(map(int, input().split()))
    # B에 대해 입력받는 값
    B = list(map(int, input().split()))
    # A, B가 낸 카드들은 1번째부터 입력된다.
    card_A = A[1:]
    card_B = B[1:]
    # 모양별로 카드의 개수를 셀 리스트를 만든다.
    # 각 인덱스를 사용하기 위해 4개가 아닌 5개를 만들었다.
    card_count_A = [0] * 5
    card_count_B = [0] * 5

    # A가 낸 카드의 모양별 개수 카운팅
    for i in card_A:
        card_count_A[i] += 1
    # B가 낸 카드의 모양별 개수 카운팅
    for j in card_B:
        card_count_B[j] += 1

    # 모양별로 비교하면서 승패를 결정한다. 
    # 4: 별 > 3: 동그라미 > 2:네모 > 1: 세모  
    for k in range(4, 0, -1):
        if card_count_A[k] == card_count_B[k]:
            continue
        elif card_count_A[k] > card_count_B[k]:
            print('A')
            break
        else:
            print('B')
            break
    else:
        print('D')