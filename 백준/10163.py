N = int(input())

# 빈 종이를 의미하는 2차원 배열 생성 (요소는 모두 0이다)
paper = [[0 for i in range(1001)] for j in range(101)]

for i in range(1, N + 1):
    x, y, width, height = map(int, input().split())

    # 너비와 높이만큼 해당 좌표에서 색종이를 덮는다.
    # 앞에 있는 색종이가 뒤에 할당되어서 덮어진다.
    for w in range(width):
        for h in range(height):
            paper[x + w][y + h] = i

# 색종이의 면적을 구한다.
for j in range(1, N + 1):
    area = 0
    for _ in range(1001):
        area += paper[_].count(j)
    print(area)



