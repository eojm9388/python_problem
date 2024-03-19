T = int(input())

# 아래쪽, 오른쪽, 오른쪽 대각선, 왼쪽 대각선
di = [1, 0, 1, 1]
dj = [0, 1, 1, -1]

def check(i, j):
    # 방향 선택
    for n in range(4):
        # 개수 선택
        for power in range(1, 5):
            ni = i + di[n] * power # 중요
            nj = j + dj[n] * power

            if not (0<=ni<N and 0<=nj<N):
                break
            if filed[ni][nj] == '.':
                break

        else:
            return True


for tc in range(1, T+1):
    N = int(input())

    filed = [list(input()) for _ in range(N)]
    result = 'NO'
    for i in range(N):
        for j in range(N):
            if filed[i][j] == 'o':
                if check(i, j):
                    result  = 'YES'
                    break
        if result == 'YES':
            break
    print(f'#{tc}', result)