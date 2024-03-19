# import sys
# sys.stdin = open('input.txt')

def f(n):
    # 정점이 트리에 존재한다면
    if n != 0:
        # 연산자라면 왼쪽 자식과 오른쪽 자식을 연산 해줘야함
        if tree[n][0] in '+-*/':
            if tree[n][0] == '+':
                return f(int(tree[n][1])) + f(int(tree[n][2]))
            elif tree[n][0] == '-':
                return f(int(tree[n][1])) - f(int(tree[n][2]))
            elif tree[n][0] == '*':
                return f(int(tree[n][1])) * f(int(tree[n][2]))
            elif tree[n][0] == '/':
                return f(int(tree[n][1])) / f(int(tree[n][2]))
        # 피연산자라면 해당 값을 숫자로 바꿔서 리턴
        else:
            return int(tree[n][0])


for tc in range(1, 11):
    # 정점의 개수 N
    N = int(input())
    # [현재 정점 값, 왼쪽 자식 정점 번호, 오른쪽 자식 정점 번호]
    tree = [[0, 0, 0] for _ in range(N+1)]

    # 트리 갱신
    for i in range(N):
        # 정점의 정보
        line = list(input().split())
        # 정점의 번호 node, 정점의 값 val
        node, val = int(line[0]), line[1]
        # 트리의 값 부분 할당
        tree[node][0] = val
        # 정점의 값이 연산자라면 자식들이 있다
        if val in '+-*/':
            # 정점의 자식들 대입
            tree[node][1] = line[2]
            tree[node][2] = line[3]
    # print(tree)
    # 트리의 루트부터 함수 실행
    print(f'#{tc}', int(f(1)))

