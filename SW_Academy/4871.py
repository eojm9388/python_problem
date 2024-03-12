# import sys
# sys.stdin = open('input.txt')

T = int(input())

# DFS
def dfs(S, G):
    # 출발노드 방문
    v = S
    top = -1
    visited[v] = True
    # 모든 노드 방문
    while True:
        # 현재 노드의 인접한 노드 탐색
        for w in edge_map[v]:
            # 방문 안한 노드가 있다면
            if not visited[w]:
                # 방문 처리
                visited[w] = True
                # 만약 원하는 도착노드라면 성공 리턴
                if w == G:
                    return 1
                # 아니면 push
                top += 1
                stack[top] = v
                # 현재 노드 갱신
                v = w
                break
        # 현재 노드에 인접한 노드가 없다면
        else:
            # 스택에 노드가 들어있다면
            if top > -1:
                # pop
                top -= 1
                # 이전 노드로 되돌아감
                v = stack[top+1]
            # 없으면 더이상 방문할 노드가 없음
            else:
                return 0


for tc in range(1, T+1):
    # 노드, 간선 개수
    V, E = map(int, input().split())
    # 간선 연결 2차원 리스트
    edge_map = [[] for _ in range(V+1)]
    # 방문 기록
    visited = [False] * (V+1)
    # 스택 생성
    stack = [0] * (V + 10)

    # 간선으로 연결된 노드 추가
    for e in range(E):
        # 간선 정보
        edge = list(map(int, input().split()))
        # 한방향이니깐 1번
        edge_map[edge[0]].append(edge[1])
        # 무방향이면 2번 해줘야함
        # edge_map[edge[1]].append(edge[0])
    # 출발노드 S, 도착노드 G
    S, G = map(int, input().split())

    print(f'#{tc}', dfs(S, G))