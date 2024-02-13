# import sys
# sys.stdin = open('input.txt')

T = int(input())

def f(fx):
    # 스택 생성
    top = -1
    stack = [None] * 300
    # 연산 코드 순회
    for tk in fx:
        # 토근이 마지막 점이라면
        if tk == '.':
            # 스택에 남아있는게 1개가 아니라면
            if top != 0:
                # 연산 불가
                return 'error'
            # 남아있는게 1개라면 반환
            else:
                return stack[top]
        # 토큰이 연산자라면
        elif tk in '+-*/':
            # 스택에 피연산자가 2개 미만이라면 연산 불가
            if top < 1:
                return 'error'
            # 2개 pop해서 연산하기
            top -= 1
            # 위에 있는 숫자가 B
            B = stack[top + 1]
            # 아래 숫자가 A
            top -= 1
            A = stack[top + 1]
            # 연산 결과를 다시 스택에 push
            top += 1
            # 연산자별로 계산
            if tk == '+':
                stack[top] = A + B
            elif tk == '-':
                stack[top] = A - B
            elif tk == '*':
                stack[top] = A * B
            elif tk == '/':
                # 0으로는 못 나눈다
                if B == 0:
                    return 'error'
                # /만 한다면 결과값으로 실수가 나온다
                else:
                    stack[top] = A // B

        else:
            # 피연산자라면 정수로 바꿔 스택에 push
            top += 1
            stack[top] = int(tk)


for tc in range(1, T+1):
    fx = list(input().split(' '))
    print(f'#{tc}', f(fx))
