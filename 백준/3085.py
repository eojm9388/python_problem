N = int(input())

MAP = [list(input()) for _ in range(N)]

di = [0, 1]
dj = [1, 0]
def change(i, j, d):
    ni = i + di[d]
    nj = j + dj[d]
    # 바꿔줄 사탕이 범위안에 있고 다른 색깔의 사탕이라면 바꿔준다
    if 0<=ni<N and 0<=nj<N and MAP[ni][nj] != MAP[i][j]:
        MAP[ni][nj], MAP[i][j] = MAP[i][j], MAP[ni][nj]
        # 연속된 사탕 개수 구하기
        count()
        # 원위치
        MAP[ni][nj], MAP[i][j] = MAP[i][j], MAP[ni][nj]


def count():
    global max_cnt
    # 연속된 사탕 개수 구하기
    for i in range(N):
        # 행 개수, 열 개수
        cnt_i, cnt_j = 1, 1

        for j in range(1, N):
            # 전의 사탕과 같은색이면 개수 증가
            if MAP[i][j-1] == MAP[i][j]:
                cnt_i += 1
            # 아니면 초기화
            else:
                cnt_i = 1
            if MAP[j-1][i] == MAP[j][i]:
                cnt_j += 1
            else:
                cnt_j = 1
            # 최대 개수 갱신
            max_cnt = max(max_cnt, cnt_i, cnt_j)


max_cnt = 0

# 모든 좌표의 사탕을 우-하로 바꿔준 뒤 연속된 사탕의 개수를 구한다.
for i in range(N):
    for j in range(N):
        for k in range(2):
            change(i, j, k)

print(max_cnt)