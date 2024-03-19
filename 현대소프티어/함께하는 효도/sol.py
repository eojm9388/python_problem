# 중복되지 않는 순열을 만들어줄 라이브러리
from itertools import permutations

# 친구 1명당 최대 수확물과 그 때 path를 구하는 함수
# f(위치, 위치, 이동 횟수, 현재까지 수확량]
def f(x, y, i, c):
    global max_cnt
    # 3회 이동 했으면 최대 수확량과 path 갱신
    if i == 3:
        if max_cnt < c:
            max_cnt = c
            # 깊은 복사로 복사
            temp_2 = path[:]
            # 마지막으로 최댓값이 갱신된게 제일 큰 값이다
            path_result.append(temp_2)
        return
		# 델타 탐색
    for n in range(4):
        nx = x + dx[n]
        ny = y + dy[n]
				# 범위안이고 방문한 곳이 아라면 탐색
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            # 방문처리
            visited[nx][ny] = 1
            # path 기록
            path.append([nx, ny])
            # 위치 이동 (이동 횟수 증가, 열매 수확량 증가)
            f(nx, ny, i+1, c+temp)
            # 초기화
            visited[nx][ny] = 0
            path.pop()


# 격자 크기 N, 친구 수 M
N, M = map(int, input().split())
# 열매 밭
MAP = [list(map(int, input().split())) for _ in range(N)]
# 친구들의 위치
friends = [list(map(int, input().split())) for _ in range(M)]

# 델타 탐색
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 열매 수확량의 최댓값들을 모아둔 리스트
result_list = []

# permutations를 쓰는 이유: 위의 f함수를 돌리면 친구들의 위치 좌표의 순서에 따라
# 열매의 수확량이 다르다. 그렇기 때문에 나올 수 있는 친구의 위치 좌표 순서를 모두 실행해본다
for arr in permutations(friends):
		# 친구 전체의 수확물 양
    result = 0
    # 열매를 수확하면 남아있는 열매가 0이 되므로 MAP값을 수정해야한다.
    # 따라서 임시 MAP 리스트를 만들어 사용한다.
    temp_MAP = [MAP[x][:] for x in range(N)]
    # print(temp_MAP)
    # 친구의 위치좌표 friend
    for friend in arr:
			  # 친구 한명당 수확할 수 있는 최대 열매 개수
        max_cnt = 0
        # 최대 수확값을 갱신할 때 이동했던 경로를 저장할 path
        path = []
			  # 최대 수확값이 여러번 갱신되기 때문에 path를 저장할 리스트
        # path_result의 마지막 path가 최댓값일 때 path이다
        path_result = []
        # 방문처리 해줄 리스트
        visited = [[0] * N for _ in range(N)]
        # 친구의 위치 좌표
        x, y = friend[0]-1, friend[1]-1
        visited[x][y] = 1
        # 함수 실행
        f(x, y, 0, temp_MAP[x][y])
        # 함수를 실행하면 현재 친구가 수확할 수 있는 최대 열매의 개수 max_cnt와
        # 그 때 경로가 path_list[-1]에 담겨져 있다.
        temp_MAP[x][y] = 0
        # 수확한 경로의 열매 제거
        for p in path_result[-1]:
            temp_MAP[p[0]][p[1]] = 0
		    # 수확물에 추가
        result += max_cnt
    result_list.append(result)

print(max(result_list))