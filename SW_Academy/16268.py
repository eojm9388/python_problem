import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # 풍선안의 꽃가루. 2차원 배열
    balloon = [list(map(int, input().split())) for _ in range(N)]
    # 꽃가루의 최대합
    flowers_max = 0
    # 모든 좌표값 순회
    for i in range(N):
        for j in range(M):
            # 현재 좌표의 꽃가루
            flowers = balloon[i][j]
            # 현재 좌표값의 4방향 인접 꽃가루 더하기
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni = i + di
                nj = j + dj
                # 인접한 곳이 범위를 벗어나지 않을 경우만 더하기
                if 0<=ni<N and 0<=nj<M:
                    flowers += balloon[ni][nj]
            # 꽃가루 최대합 갱신
            if flowers > flowers_max:
                flowers_max = flowers

    print(f'#{test_case}', flowers_max)


