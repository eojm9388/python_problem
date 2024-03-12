# import sys
# sys.stdin = open('input.txt')

# 숫자 암호화 규칙
CODE = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

T = int(input())

for tc in range(1, T+1):
    # 세로 N, 가로 M
    N, M = map(int, input().split())
    # 암호코드 숫자
    code = ''
    # 결과값
    result = 0
    for i in range(N):
        # 양쪽 문자열에 0 제거
        # 0만 있다면 빈 문자열
        line = input().strip('0')
        n = len(line)
        # 빈 문자열이 아니라면 그 코드 한줄만 해석하면 된다.
        if n:
            code_line = line.zfill(56)

    # 7자리씩 숫자로 변경
    for j in range(0, 56, 7):
        code_one = code_line[j:j+7]
        # 숫자 암호화 규칙의 인덱스값이 숫자값
        code += str(CODE.index(code_one))
    # 홀수 자리합, 짝수 자리 합
    odd = even = 0
    for c in range(8):
        # 인덱스 + 1 -> n번 자리 숫자 -> 반대로
        if c % 2 == 0:
            odd += int(code[c])
        else:
            even += int(code[c])
        # 각 자리 합 구하기
        result += int(code[c])
    
    # 10의 배수가 아니면 0 
    if (odd*3+even) % 10:
        print(f'#{tc}', 0)
    # 10의 배수면 각 자리 합 출력
    else:
        print(f'#{tc}', result)

