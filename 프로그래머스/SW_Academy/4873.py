# import sys
# sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 입력받은 문자열
    word = list(input())
    # 스택 생성
    stack = []
    top = -1
    # 문자열 순회
    for w in range(len(word)):
        # 만약 스택에 아무것도 없다면
        if top == -1:
            # push
            top += 1
            stack.append(word[w])
        # 스택에 요소가 있다면
        else:
            # 앞에 문자와 중복된다면
            if word[w] == stack[top]:
                # pop
                top -= 1
                stack.pop()
            # 앞에 문자와 다르다면
            else:
                # push
                top += 1
                stack.append(word[w])

    print(f'#{tc}', len(stack))

