# import sys
# sys.stdin = open('input.txt')

A, B = 0, 99

def DFS(A, B):
    # 시작노드
    v = A
    # 시작노드 방문
    visited[v] = True
    # top 선언
    top = -1
    # 모든 노드 탐색
    while True:
        # 현재노드와 인접한 노드 탐색
        for w in adjl[v]:
            # 방문한 기록이 없다면
            if not visited[w]:
                # 방문 처리
                visited[w] = True
                # 만약 도착노드라면 성공
                if w == B:
                    return 1
                # 아니면 스택에 push
                top += 1
                stack[top] = v
                # 현재노드 갱신
                v = w
                break
        # 현재 노드에 인접한 방문한 적 없는 노드가 없다면
        else:
            # 스택에 이전에 탐색한 노드가 있다면
            if top > -1:
                # 스택에 pop
                top -= 1
                # 이전 노드로 되돌아가기
                v = stack[top+1]
            # 스택에 노드가 없다면 실패
            else:
                return 0


for t in range(10):
    # 테스트케이스 tc, 길의 총 개수 E
    tc, E = map(int, input().split())
    # 방문 기록 리스트
    visited = [False] * (B+1)
    # 스택 생성
    stack = [0] * (B+1)
    # 간선 정보 2차원 리스트
    adjl = [[] for _ in range(B+1)]
    # 간선 입력
    edge = list(map(int, input().split()))
    # 간선 정보 리스트에 입력값 넣기
    for i in range(E):
        n1, n2 = 2*i, 2*i+1
        # 한방향
        adjl[edge[n1]].append(edge[n2])

    print(f'#{tc}', DFS(A, B))


