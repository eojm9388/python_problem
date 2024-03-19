import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    A, B = input().split()
    # 문자열 A와 B의 길이
    N, M = len(A), len(B)
    # 문자열 A 내의 문자열 B의 개수
    count = 0
    # 인덱스
    i = 0
    while i < N:
        # 만약 A의 i에서 B를 찾았다면
        if A[i:i+M] == B:
            # 개수 증가 후 B의 길이만큼 인덱스 증가
            count += 1
            i += M
        # 아니라면 인덱스 1 증가
        else:
            i += 1

    # 타이핑 횟수 = A의 길이 - B의 개수 * (B의 길이 - 1) -> 카운트도 한번 포함되므로
    result = N - count*(M-1)

    print(f'#{tc}', result)
