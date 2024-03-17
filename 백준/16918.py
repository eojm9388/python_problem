R, C, N = map(int, input().split())

# 폭탄의 현재 위치
MAP = [list(input()) for _ in range(R)]
# 폭탄이 몇초에 생긴건지 확인하기 위해 만듬
visited = [[0] * C for _ in range(R)]

# 짝수일 때는 폭탄이 빈 곳에 폭탄을 놓는다
def cycle_even(idx):
    for i in range(R):
        for j in range(C):
            if visited[i][j] == 0:
		            # 폭탄을 놓는 시간을 넣는다
                visited[i][j] = idx

# 홀수일 때는 3초전 폭탄이 터진다.
def cycle_odd(idx):
    for i in range(R):
        for j in range(C):
		        # 인접한 곳에 폭탄이 있다면 그 폭탄은 나중에 터져야함
            temp = visited[i][j]
            # 처음 visited를 1로 했기 때문에 3은 예외처리
            if idx == 3:
                idx += 1
            # 3초가 지난 폭탄이라면 인접 폭발    
            if visited[i][j] == idx-3:
                visited[i][j] = 0
                for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    ni = i + di
                    nj = j + dj        # 인접한 곳에 터질 폭탄이 있다면 거긴 나중에 터짐
                    if 0<=ni<R and 0<=nj<C and visited[ni][nj] != temp:
                        visited[ni][nj] = 0


# 초기 폭탄 위치 설정
for i in range(R):
    for j in range(C):
        if MAP[i][j] == 'O':
            visited[i][j] = 1

idx = 2
# 시간에 따라 폭탄의 위치를 갱신해줌
while idx <= N:
    cycle_even(idx)
    idx += 1
    if idx > N:
        break
    cycle_odd(idx)
    idx += 1

# 0 초과인 부분에는 폭탄이 위치함
for i in range(R):
    for j in range(C):
        if visited[i][j] > 0:
            visited[i][j] = 'O'
        else:
            visited[i][j] = '.'

for k in range(R):
    print(''.join(visited[k]))


