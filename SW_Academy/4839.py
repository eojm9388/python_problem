import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 이진 탐색
def binary_search(s, e, k):
    # 몇번만에 원하는 페이지를 찾았는지 반환
    count = 1
    while s <= e:
        c = int((s + e) / 2)
        # print('중간값:', c)
        if c == k:
            # print(f'{count}번만에 찾았다!')
            return count
        elif c < k:
            s = c
        elif c > k:
            e = c
        # print(f'{count}번째 찾는중')
        count += 1
    # print('못찾았다')
    return -1



for test_case in range(1, T + 1):
    N, Pa, Pb = map(int, input().split())
    # A가 탐색한 횟수
    count_A = binary_search(1, N, Pa)
    # print(f'A는 {count_A}번만에 찾았다.')

    # B가 탐색한 횟수
    count_B = binary_search(1, N, Pb)
    # print(f'B는 {count_B}번만에 찾았다.')

    # 탐색 횟수가 적은 사람이 이긴다.
    if count_A < count_B:
        print(f'#{test_case} A')
    elif count_B < count_A:
        print(f'#{test_case} B')
    else:
        print(f'#{test_case} 0')

