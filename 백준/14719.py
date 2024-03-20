# 높이와 너비
H, W = map(int, input().split())
# 블록의 높이들
height = list(map(int, input().split()))

# 블록이 있는 부분을 1처리
visited = [[0] * H for _ in range(W)]
for w in range(W):
    for h in range(height[w]):
        visited[w][h] = 1

# 풀이방법: 양쪽 끝 위부터 조사 -> 만약 블록이 없다면 그 줄 다 블록처리
# 블럭 처리하고 남은 0이 빗물이 고일 수 있는 부분이다.

#ex) 3 0 1 4
#
#  0 0 0 1             1 1 1 1
#  1 0 0 1  왼쪽 위     1 0 0 1
#  1 0 0 1  조사 후     1 0 0 1
#  1 0 1 1  1 처리      1 0 1 1

# 왼쪽 위부터 확인
jdx = 0
for i in range(H):
    if visited[0][-i-1] == 0:
        while jdx < W and visited[jdx][-i-1] == 0:
            visited[jdx][-i-1] = 1
            jdx += 1
        jdx = 0

# 오른쪽 위도 확인
jdx = -1
for i in range(H):
    if visited[-1][-i-1] == 0:
        while jdx > -W and visited[jdx][-i-1] == 0:
            visited[jdx][-i-1] = 1
            jdx -= 1
        jdx = -1

# 0 개수 세기
cnt = 0

for i in range(W):
    cnt += visited[i].count(0)

print(cnt)


