T = int(input())

# 카페는 대각선 4방향으로만 갈 수 있다.
#        1          2         2
#     2     4    1     3   3     1
#        3          4         4
# 위의 모든 경우는 다 같은 경우 임으로 카페를 가는 방향 순서를 하나로 결정
# 아래왼 -> 아래오른 -> 위오른 -> 위왼
MOVE = [[1, -1], [1, 1], [-1, 1], [-1, -1]]


# 카페를 이동하는 함수
def f(i, j, d):
    # 위왼쪽 좌표가 출발 좌표랑 같은 지점이고, 지금 이동 방향이 위왼이면 한바퀴 다 돈거임
    if [i - 1, j - 1] == cafe_start and d == 3:
        # 카페 이동 경로 저장
        temp = cafe_path[:]
        cafe_path_list.append(temp)
        return
    # 이상한 방향 -> 인덱스 에러 방지
    if d == 4:
        return
    # 다음 카페의 좌표
    ni = i + MOVE[d][0]
    nj = j + MOVE[d][1]

    # 범위안에 있어야함
    if 0 <= ni < N and 0 <= nj < N:
        # 이미 먹었던 디저트라면 실패
        if cafe[ni][nj] in cafe_path:
            return
        # 갔던 방향으로 한번 더 가보기
        cafe_path.append(cafe[ni][nj])
        f(ni, nj, d)
        # 초기화
        cafe_path.pop()
        # 다음 방향으로 전환 후 가보기
        cafe_path.append(cafe[ni][nj])
        f(ni, nj, d + 1)
        # 초기화
        cafe_path.pop()


for tc in range(1, T + 1):
    N = int(input())
    # 카페 디저트 종류
    cafe = [list(map(int, input().split())) for _ in range(N)]
    # print(cafe)
    # 카페 경로 리스트
    cafe_path_list = []

    # 완전 탐색
    for i in range(N):
        # 갈때는 대각선 왼쪽, 올때는 대각선 오른쪽을 무조건 가야하기 때문에
        # 양쪽 1줄은 시작점이 되지 못한다
        for j in range(1, N - 1):
            # 처음 출발점
            cafe_path = [cafe[i][j]]
            cafe_start = [i, j]
            f(i, j, 0)
    max_cnt = 0
    # 디저트를 가장 많이 먹을 때 개수 구하기
    for path in cafe_path_list:
        cnt = len(path)
        if max_cnt < cnt:
            max_cnt = cnt
    # 디저트를 먹을 수 없는 경우
    if max_cnt == 0:
        max_cnt = -1
    print(f'#{tc}', max_cnt)