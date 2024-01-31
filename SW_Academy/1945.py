import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # 소인수 분해할 수
    N = int(input())
    # 각 수의 지수 [2, 3, 5, 7, 11]
    result = [0, 0, 0, 0, 0]
    # 1이 될때까지 나눗셈
    while N > 1:
        # 2의 지수 구하기
        if N % 2 == 0:
            result[0] += 1
            N //= 2
        # 3의 지수 구하기
        elif N % 3 == 0:
            result[1] += 1
            N //= 3
        # 5의 지수 구하기
        elif N % 5 == 0:
            result[2] += 1
            N //= 5
        # 7의 지수 구하기
        elif N % 7 == 0:
            result[3] += 1
            N //= 7
        # 11의 지수 구하기
        elif N % 11 == 0:
            result[4] += 1
            N //= 11

    print(f'#{test_case}', *result)