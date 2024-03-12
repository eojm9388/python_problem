# 노드의 개수
N = int(input())
# 간선 정보를 담을 리스트
edge = [[] for _ in range(N+1)]
# 부모 노드의 번호를 담을 트리의 리스트
tree = [[] for _ in range(N+1)]
# 간선 정보 저장
for i in range(N-1):
    A, B = map(int, input().split())

    edge[A].append(B)
    edge[B].append(A)

# 깊이 우선 탐색을 한다.
# 깊이 우선 탐색을 하게 되면 자신의 자식들을 먼저 보는데
# 이때 자식을 방문처리할 때 부모의 정보를 tree에 넣어준다.

def DFS():
    stack = [1]
    visited = [0] * (N+1)

    while stack:
        v = stack.pop()

        for j in edge[v]:
            if visited[j] == 0:
                visited[j] = 1
                tree[j].append(v)
                stack.append(j)

DFS()
# 부모의 정보는 2번 노드부터 출력한다.
for i in range(2, N+1):ㅁ
    print(*tree[i])
