# DFS(세로 좌표, 가로 좌표, 현재 방문했던 지점)
def DFS(i, j, k):
    global cnt
    # 만약 마지막 지점에 도달했다면 경우의 수 추가
    # 델타 탐색으로 오기 때문에 마지막 지점에 도달만 한다면 모든 경우가 다 다르다
    if k == m - 1:
        cnt += 1
        return
		# 델타 탐색
    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ni = i + di
        nj = j + dj
        # 범위 안이고 방문 하지 않은 곳이고, 벽이 아닌 곳이면 간다.
        if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == False and MAP[ni][nj] == 0:
            # 만약 다음 방문 좌표가 다음 지점보다 나중 지점이면 안된다
            if [ni+1, nj+1] in arr[k + 2:]:
                continue
            # 아니라면 다음 지점 or 갈 수 있는 곳
            visited[ni][nj] = True
            # 만약 다음 방문 좌표가 다음 지점이라면 현재 방문한 지점을 1 올리고 다음 탐색
            if [ni, nj] == [arr[k + 1][0]-1, arr[k + 1][1]-1]:
                DFS(ni, nj, k + 1)
            # 아니라면 그냥 델타 탐색 계속
            else:
                DFS(ni, nj, k)
            # 방문 초기화
            visited[ni][nj] = False

# 격자 사이즈 n, 방문할 지점 개수 m
n, m = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(n)]
# 방문할 좌표 리스트 -> 입력받은 순서대로 방문해야한다
arr = [list(map(int, input().split())) for _ in range(m)]
# 방문처리해줄 리스트
visited = [[False] * n for _ in range(n)]
# 방문 가능한 경우의 수
cnt = 0
# 시작점 방문 처리
visited[arr[0][0]-1][arr[0][1]-1] = True
# DFS(세로 좌표, 가로 좌표, 현재 방문했던 지점) 실행 -> 처음에는 0번 좌표부터 시작한다
DFS(arr[0][0]-1, arr[0][1]-1, 0)
print(cnt)

