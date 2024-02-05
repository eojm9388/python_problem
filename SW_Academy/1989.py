import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 입력받은 문자열
    str1 = input()
    # 뒤집은 문자열
    str2 = str1[::-1]

    print(f'#{tc}', end=' ')
    # 입력받은 문자열이 뒤집은 문자열과 같다면 회문이다.
    if str1 == str2:
        print(1)
    else:
        print(0)

