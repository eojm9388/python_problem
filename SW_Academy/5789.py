import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, Q = map(int, input().split())
    # 현주가 가지고 있는 숫자 박스
    number_box = [0] * N
    # Q회 동안 숫자 변경
    # 인덱스0이 1번 상자
    for i in range(1, Q+1):
        # 바꿀 상자의 범위 입력
        L, R = map(int, input().split())
        # 상자의 숫자 변경
        for j in range(L-1, R):
            number_box[j] = i
    print(f'#{test_case}', *number_box)