C, R = map(int, input().split())

K = int(input())
# 좌석 배치도
seat = [[0] * C for _ in range(R)]
# 좌석을 배치할때 추가시킬 방향
# 상:1, 우:2, 하:3, 좌:4
direction = 1 # 상
# 현재 좌석 번호
count = 1
# 상하좌우 범위를 제한하기위해 만든 변수
up, down , right, left = 0, 1, 1, 1

# 시작 좌표
i, j = R-1, 0

# 결과값
result = 0
# 좌석을 모두 배치할 때까지 반복
while count <= R*C:
    # print('i:', i, 'j:',j)
    # 만약 좌석배치가 안되었다면
    if seat[i][j] == 0:
        # 좌석배치
        seat[i][j] = count
        count += 1
        # 현재 좌석배치 방향이 '상'이라면 위쪽으로 배치
        if direction == 1:
            # print('상')
            i -= 1
            # 만약 제한범위에 도달했으면 좌석배치방향을 '우'로 바꿈
            if i == up:
                direction = 2
                # 제한범위가 늘어남
                up += 1
        # 현재 좌석배치 방향이 '우'이라면 오른쪽으로 배치
        elif direction == 2:
            # print('우')
            j += 1
            # 만약 제한범위에 도달했으면 좌석배치방향을 '하'로 바꿈
            if j == C - left:
                direction = 3
                right += 1
        # 현재 좌석배치 방향이 '하'이라면 아래쪽으로 배치
        elif direction == 3:
            # print('하')
            i += 1
            # 만약 제한범위에 도달했으면 좌석배치방향을 '좌'로 바꿈
            if i == R - down:
                direction = 4
                down += 1
        # 현재 좌석배치 방향이 '좌'라면 왼쪽으로 배치
        elif direction == 4:
            # print('좌')
            j -= 1
            # 만약 제한범위에 도달했으면 좌석배치방향을 다시'상'으로 바꿈
            if j == left:
                direction = 1
                left += 1

# 원하는 좌석을 2차원 배열 모두 순회하여 찾는다.
for y in range(R):
    for x in range(C):
        if seat[y][x] == K:
            # x, y 좌표가 리스트의 2차원 배열 인덱스와 달라 변경해준다.
            result = (x+1, R-y)
            break
    if result != 0:
        break

if result == 0:
    print(0)
else:
    print(result[0], result[1])



