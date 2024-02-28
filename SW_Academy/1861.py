T = int(input())

for tc in range(1, T+1):
    # 방 크기 N
    N = int(input())
    # 방 번호 2차원 리스트
    MAP = [list(map(int, input().split())) for _ in range(N)]
    # 최대 이동할 수 있는 방의 번호
    position = []
    # 최대 이동 횟수
    max_path_count = 0
    # 전체 순회
    for i in range(N):
        for j in range(N):
            # 시작한 방번호 기록
            x, y = i, j
            # 방 이동 횟수
            cnt = 1
            while True:
                # 방 이동을 상하좌우 모두 실패하면 거기서 이동할 곳이 없다 -> 종료조건
                fail = 0
                # 델타 탐색
                for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    ni = i + di
                    nj = j + dj
                    # 방을 이동할 수 있는 조건
                    if 0<=ni<N and 0<=nj<N and MAP[i][j]+1 == MAP[ni][nj]:
                        # 방을 이동 했으니깐 현재 방 번호 갱신
                        cnt += 1
                        i, j = ni, nj
                        break
                    # 방 이동 실패
                    else:
                        fail += 1
                # 방을 상하좌우로 이동하는게 실패했다면 거기가 마지막 방이다
                if fail == 4:
                    break
            
            # 최대 이동 횟수 갱신 -> 이때 방 번호를 기록
            if max_path_count < cnt:
                max_path_count = cnt
                # position에 이전 최대이동횟수일때 방번호들이 있어서 초기화
                position = []
                position.append(MAP[x][y])
            # 최대 이동 횟수가 같다면 제일 작은 방 번호를 출력해야하기 때문에 기록
            elif max_path_count == cnt:
                position.append(MAP[x][y])
    # 최대 이동 횟수이면서 방번호가 제일 작은 방을 출력
    print(f'#{tc}', min(position), max_path_count)

