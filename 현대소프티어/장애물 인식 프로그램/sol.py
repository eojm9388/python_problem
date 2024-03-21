from collections import deque

# 장애물에 인접한 장애물 모두를 방문 처리
def BFS(i, j):
    q = deque()
    q.append([i, j])
    # 장애물 개수 세기
    cnt = 0
    while q:
        v = q.popleft()
        i, j = v[0], v[1]

        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append([ni, nj])
                cnt += 1
    # 장애물이 몇개인지 반환
    return cnt + 1



N = int(input())

MAP = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

# 장애물의 도로(벽)를 모두 방문처리
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 0:
            visited[i][j] = 1
# 장애물 구역이 몇개인지 세기
cnt = 0
# 장애물 구역 당 장애물이 몇개 있는지 넣기
block = []
for i in range(N):
    for j in range(N):
        # 탐색한 장애물 구역이 아니라면
        if visited[i][j] == 0:
            cnt += 1
            visited[i][j] = 1
            block.append(BFS(i, j))


print(cnt)
# 장애물 개수로 오름차순
block.sort()
for i in range(len(block)):
    print(block[i])