from collections import deque
N, K = map(int, input().split())

time = [0] * (100001)
visited = [0] * (100001)

visited[N] = 1
q = deque([N])

while q:
    p = q.popleft()

    if p == K:
        print(time[p])
        break

    for i in [1, -1]:
        if 0<= p+i <= 100000 and visited[p+i] == 0:
            time[p+i] = time[p] + 1
            visited[p+i] = 1
            q.append(p+i)

    if 2*p<=100000 and visited[2*p] == 0:
        time[2*p] = time[p] + 1
        visited[2*p] = 1
        q.append(2*p)

