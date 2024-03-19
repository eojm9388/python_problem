# import sys
# sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 자리 수 N, N자리 16진수 Hex
    N, Hex = input().split()
    # 정수로 형 변환
    N = int(N)
    # 16진수로 변환
    Hex = int(Hex, 16)
    # zfill(N): 문자열의 길이가 N이 될때까지 앞에 0을 붙임
    print(f'#{tc}', format(Hex, 'b').zfill(4*N))