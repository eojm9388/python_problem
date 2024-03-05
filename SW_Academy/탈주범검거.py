T = int(input())

# d = 1, 2, 3, 4 [상, 하, 좌, 우] 방향

# 위로 움직이기
def move_up(x, y, l, d):
    nx = x - 1
    ny = y
    # 이동하는 곳이 범위안에 있어야하고 이동할려고 하는 통로 모양이 아래쪽이 열려있는 모양이어야 한다
    if nx >= 0 and (MAP[nx][ny] in [1, 2, 5, 6]):
        if arrival_point[nx][ny] == 0:
            arrival_point[nx][ny] = 1
        move_point(nx, ny, l+1, 1)

# 아래로 움직이기
def move_down(x, y, l, d):
    nx = x + 1
    ny = y
    # 이동하는 곳이 범위안에 있어야하고 이동할려고 하는 통로 모양이 위쪽이 열려있는 모양이어야 한다
    if nx < N and (MAP[nx][ny] in [1, 2, 4, 7]):
        if arrival_point[nx][ny] == 0:
            arrival_point[nx][ny] = 1
        move_point(nx, ny, l+1, 2)



# 왼쪽으로 움직이기
def move_left(x, y, l, d):
    nx = x
    ny = y - 1
    # 이동하는 곳이 범위안에 있어야하고 이동할려고 하는 통로 모양이 오른쪽이 열려있는 모양이어야 한다
    if ny >= 0 and (MAP[nx][ny] in [1, 3, 4, 5]):
        if arrival_point[nx][ny] == 0:
            arrival_point[nx][ny] = 1
        move_point(nx, ny, l+1, 3)


# 오른쪽으로 움직이기
def move_right(x, y, l, d):
    nx = x
    ny = y + 1
    # 이동하는 곳이 범위안에 있어야하고 이동할려고 하는 통로 모양이 왼쪽이 열려있는 모양이어야 한다
    if ny < M and (MAP[nx][ny] in [1, 3, 6, 7]):
        if arrival_point[nx][ny] == 0:
            arrival_point[nx][ny] = 1
        move_point(nx, ny, l+1, 4)


# 통로 설정
def move_point(x, y, l, d):
    # 만약 움직일 수 있는 시간이 다 됐다면 끝
    if l == L:
        return

    # 1번 통로모양이라면 상하좌우로 모두 이동할 수 있다.
    if MAP[x][y] == 1:
        # 만약 갔던 곳에서 돌아오지 않는다면 이동
        # 예) 왼쪽 통로에서 다시 오른쪽 통로로 이동하면 원위치로 돌아오는 것
        # 위와 같은 경우를 빼주었다 -> 가지치기
        if d != 2:
            move_up(x, y, l, d)
        if d != 1:
            move_down(x, y, l, d)
        if d != 4:
            move_left(x, y, l, d)
        if d != 3:
            move_right(x, y, l, d)

    # 2번 통로모양이라면 상하로 이동할 수 있다.
    elif MAP[x][y] == 2:
        if d != 2:
            move_up(x, y, l, d)
        if d != 1:
            move_down(x, y, l, d)

    # 3번 통로모양이라면 좌우로 이동할 수 있다.
    elif MAP[x][y] == 3:
        if d != 4:
            move_left(x, y, l, d)
        if d != 3:
            move_right(x, y, l, d)

    # 4번 통로모양이라면 상우로 이동할 수 있다.
    elif MAP[x][y] == 4:
        if d != 2:
            move_up(x, y, l, d)
        if d != 3:
            move_right(x, y, l, d)

    # 5번 통로모양이라면 하우로 이동할 수 있다.
    elif MAP[x][y] == 5:
        if d != 1:
            move_down(x, y, l, d)
        if d != 3:
            move_right(x, y, l, d)

    # 6번 통로모양이라면 하좌로 이동할 수 있다.
    elif MAP[x][y] == 6:
        if d != 1:
            move_down(x, y, l, d)
        if d != 4:
            move_left(x, y, l, d)

    # 7번 통로모양이라면 상좌로 이동할 수 있다.
    elif MAP[x][y] == 7:
        if d != 2:
            move_up(x, y, l, d)
        if d != 4:
            move_left(x, y, l, d)


for tc in range(1, T+1):
    # 입력값 받아오기
    N, M, R, C, L = map(int, input().split())
    # 지하터널 지도
    MAP = [list(map(int, input().split())) for _ in range(N)]

    # 범죄자가 있을 수 있는 장소
    arrival_point = [[0] * M for _ in range(N)]

    # 1시간 후 맨홀 뚜껑에 범죄자 도착
    arrival_point[R][C] = 1

    move_point(R, C, 1, 0)

    # print(arrival_point)
    # 범죄자가 위치할 수 있는 장소의 개수 구하기
    cnt = 0
    for i in range(N):
        cnt += arrival_point[i].count(1)

    print(f'#{tc}', cnt)