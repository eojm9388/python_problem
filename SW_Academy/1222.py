# import sys
# sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    # 문자열 계산식
    fx = input()
    # 스택 생성
    top = -1
    stack = [None] * N
    # 후위 표현식
    postfix = ''
    # 연산자 우선순위
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}
    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    # 후위 표현식 만들기
    for tk in fx:
        # (라면 push
        if tk == '(':
            top += 1
            stack[top] = tk
        # 연산자라면
        elif tk in '+-*/':
            # 스택이 비어있다면 push
            if top == -1:
                top += 1
                stack[top] = tk
            # 아니라면 연산자 우선순위 비교
            else:
                # 현재 tk가 우선순위가 높다면 push
                if isp[stack[top]] < icp[tk]:
                    top += 1
                    stack[top] = tk
                # 낮거나 같다면 현재 tk보다 우선순위가 낮은 연산자가 나올때 까지 pop 
                else:
                    while top > -1 and isp[stack[top]] >= icp[tk]:
                        top -= 1
                        postfix += stack[top+1]
                    # 마지막으로 자신을 push
                    top += 1
                    stack[top] = tk
        # 만약 현재 tk가 )라면
        elif tk == ')':
            # 스택에서 (가 나올때 까지 pop
            while tk != '(':
                top -= 1
                postfix += stack[top + 1]
            # (는 버린다
            top -= 1
        # 피연산자라면 후위표현식에 추가
        else:
            postfix += tk
    # 마지막 남은 연산자 pop
    top -= 1
    postfix += stack[top+1]


    # 후위표현식 계산하기
    for tk in postfix:
        # 연산자라면
        if tk in '+-*/':
            # 스택에 피연산자 2개이상이라면
            if top >= 1:
                # 2개를 pop해서 연산
                top -= 1
                B = stack[top+1]
                top -= 1
                A = stack[top+1]
                top += 1
                if tk == '+':
                    stack[top] = A + B
                elif tk == '-':
                    stack[top] = A - B
                elif tk == '*':
                    stack[top] = A * B
                elif tk == '/':
                    if B != 0:
                        stack[top] = A // B
        # 피연산자라면 스택에 push
        else:
            top += 1
            stack[top] = int(tk)

    # 결과값 출력
    print(f'#{tc}', stack[top])



