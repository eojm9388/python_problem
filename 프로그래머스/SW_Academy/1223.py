# import sys
# sys.stdin = open('input.txt')

def make_postfix(fx):
    # 만들어진 후위표현식
    result = ''
    # 스택 생성
    stack = []
    # 입력 받은 계산식
    for tk in fx:
        # 현재 토큰이 연산자라면
        if tk in '+*':
            # 스택에 연산자가 들어있다면
            if stack:
                # *이라면 +가 나올때까지 pop
                if tk == '*':
                    while stack[-1] != '+':
                        result += stack.pop()
                        # 스택이 비었다면 탈출
                        if not stack:
                            break
                    # 현재 토큰을 스택에 push
                    stack.append(tk)
                # 아니라면 +
                # +라면 스택이 빌 때까지 pop
                else:
                    while stack:
                        result += stack.pop()
                    # 현재 토큰을 스택에 push
                    stack.append(tk)
            # 스택이 비어있다면 push
            else:
                stack.append(tk)
        # 현재 토큰이 피연산자라면 결과값에 추가
        else:
            result += tk
    # 게산식을 모두 순회하고 스택에 남아있는 연산자 pop
    while stack:
        result += stack.pop()
    return result



for tc in range(1, 11):
    N = int(input())
    fx = input()

    postfix = make_postfix(fx)
    numbers = []


    for tk in postfix:
        # 현재 토큰이 연산자라면
        if tk in '+*':
            # 피연산자가 담겨있는 스택에서
            # 2개의 숫자를 뽑아 연산한다.
            # 뒤에오는 숫자가 스택의 위에 있으므로 먼저 빼준다
            B = int(numbers.pop())
            A = int(numbers.pop())

            if tk == '+':
                numbers.append(A+B)
            else:
                numbers.append(A*B)
        else:
            numbers.append(tk)
    # 스택의 남아있는 값이 계산식의 결과값이다
    print(f'#{tc}', numbers[0])

