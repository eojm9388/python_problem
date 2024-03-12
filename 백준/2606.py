# 컴퓨터 개수
N = int(input())
# 연결된 컴퓨터 개수
computer = int(input())

# 무방향 그래프 형태로 연결된 컴퓨터의 간선 정보를 담을 리스트
linked_computer = [[] for _ in range(N+1)]

# 무방향 그래프기 때문에 양쪽에 다 넣어줘야함
for i in range(computer):
    A, B = map(int, input().split())

    linked_computer[A].append(B)
    linked_computer[B].append(A)

visited = [0] * (N+1)

# 깊이 우선탐색
def DFS():
    stack = [1]
    visited[1] = 1
    # 스택이 빌때까지
    while stack:
        v = stack.pop()
        # 연결된 모든 컴퓨터를 방문/감염 처리
        for j in linked_computer[v]:
            if visited[j] == 0:
                visited[j] = 1
                stack.append(j)


DFS()
# 방문 했다 -> 감염 됐다!
print(visited[2:].count(1))

