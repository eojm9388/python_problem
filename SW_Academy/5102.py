# import sys
# sys.stdin = open('input.txt')

from collections import deque

T = int(input())

def BFS(S, G):
    q = deque()
    visited[S] = 1
    q.append(S)

    while q:
        now = q.popleft()
        if now == G:
            return visited[now]-1
        for next in adj[now]:
            if visited[next] == 0:
                visited[next] = visited[now]+1
                q.append(next)

    return 0



for tc in range(1, T+1):
    V, E = map(int, input().split())

    adj = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        adj[n1].append(n2)
        adj[n2].append(n1)

    visited = [0] * (V+1)
    S, G = map(int, input().split())

    print(f'#{tc}', BFS(S, G))