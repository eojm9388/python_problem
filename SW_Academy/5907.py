# import sys
# sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 숫자의 개수 N, 회전 횟수 M
    N, M = map(int, input().split())

    numbers = list(map(int, input().split()))
    # 회전하니깐 결국 돌아온다
    M %= N

    print(f'#{tc}', numbers[M])

