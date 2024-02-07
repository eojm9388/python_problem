# import sys
# sys.stdin = open("input.txt", "r")

# 스택 클래스 생성
class Stack:
    # 생성자
    def __init__(self, lenght):
        # 스택의 길이
        self.lenght = lenght
        # 스택의 길이만큼 스택 리스트 생성
        self.data = [None] * lenght
        # 스택 top 생성
        self.top = -1
    
    # push 메서드
    def push(self, item):
        # 스택 리스트 크기를 넘을 경우
        if self.top == self.lenght:
            # 오버플로우
            print('overflow')
        # 크기를 넘지 않았다면
        else:
            # push
            self.top += 1
            self.data[self.top] = item
    
    # pop 메서드
    def pop(self):
        # 스택에 아무것도 없다면
        if self.top == -1:
            # 언더플로우
            print('underflow')
        # 스택에 있다면
        else:
            # pop
            self.top -= 1
            return self.data[self.top+1]
    
    # 스택의 top 요소 반환
    def get(self):
        return self.data[self.top]

    def __str__(self):
        return f'{[self.data]}'


for tc in range(1, 11):
    # 비밀번호의 길이, 비밀번호 입력
    lenght, password = input().split()
    # 스택 생성
    stack = Stack(int(lenght))
    
    for i in password:
        # 스택에 아무것도 없으면
        if stack.top == -1:
            # push
            stack.push(i)
        # 스택에 있다면
        else:
            # top 요소와 현재 숫자가 중복이라면 
            if stack.get() == i:
                # pop
                stack.pop()
            # 중복이 아니라면 push
            else:
                stack.push(i)
    
    print(f'#{tc}', end=' ')
    # 스택에 남아있는 비밀번호 출력
    for j in range(stack.top+1):
        print(stack.data[j], end='')

    print()

