def solution(arr):
    stack = []
    
    for i in arr:
        # 스택이 비어있다면
        if not stack:
            # 스택에 push
            stack.append(i)
        # 스택의 top과 같다면 건너뛰기
        elif stack[-1] == i:
            continue
        # 스택의 top과 다르다면 push
        else:
            stack.append(i)
    
    
    return stack