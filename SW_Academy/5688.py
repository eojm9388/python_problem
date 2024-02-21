# import sys
# sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    n = 1
    X = 1
    # X를 1씩 증가시키면서 세제곱을 찾는다
    while n <= N:
        if n == N:
            break
        else:
            X += 1
            n = X**3

    # 만약 n이 N보다 크다면 세제곱을 찾지 못하고 넘어간 것
    if n > N:
        X = -1

    print(f'#{tc}', X)
