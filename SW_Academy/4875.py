# import sys
# sys.stdin = open('input.txt')

T = int(input())

def DFS(start):
    global result
    i, j = start[0], start[1]
    # 범위에 넘어가면 탈락
    if i < 0 or i >= N or j < 0 or j >= N:
        return
    # 방문 했던 곳이라면 탈락
    elif visited[i][j]:
        return
    # 도착지점이라면 성공!
    elif miro[i][j] == 3:
        result = True
        return
    # 갈 수 있는 곳이라면 
    else:
        # 도착지점에 이미 도착했다면 
        # 코드 종료
        if result:
            return
        # 아니라면 방문처리
        visited[i][j] = True
        # 델타 탐색
        for d in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni = i + d[0]
            nj = j + d[1]
            DFS([ni, nj])


for tc in range(1, T+1):
    # 미로의 크기
    N = int(input())
    # 도착점에 도달할 수 있는지 여부
    result = False
    # 미로 맵 2차원 배열
    miro = [list(map(int, input())) for _ in range(N)]
    # 미로를 방문 했는지를 보는 2차원 배열
    visited = [[False] * N for _ in range(N)]
    # 출발점의 좌표를 담을 리스트
    start = [0, 0]
    
    for i in range(N):
        for j in range(N):
            # 미로의 출발점을 찾는다
            if miro[i][j] == 2:
                start[0], start[1] = i, j
            # 벽도 방문처리 -> 갈 수 없기 때문에
            elif miro[i][j] == 1:
                visited[i][j] = True

    DFS(start)
    print(f'#{tc}', int(result))

