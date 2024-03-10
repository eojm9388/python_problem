from collections import deque
N, K = map(int, input().split())

def BFS(n):
    q = deque([n])
    visited = [0] * 200001
    visited[n] = 1

    while q:
        v = q.popleft()
        if v == K:
            return position[v]
        if 2*v < 200000 and visited[2*v] == 0:
            visited[2*v] = 1
            q.append(2*v)
            position[2*v] = position[v]
        for i in [-1, 1]:
            if 0<= v+i < 200000 and visited[v+i] == 0:
                visited[v+i] = 1
                q.append(v+i)
                position[v+i] = position[v] + 1



position = [0] * 200001

print(BFS(N))


