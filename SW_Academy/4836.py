import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # 칠할 영역의 개수
    N = int(input())
    # 보라색 칸의 개수
    result = 0
    # 색칠할 종이의 2차원 배열
    paper = [[0] * 10 for _ in range(10)]

    # 칠할 영역의 개수만큼 반복
    for n in range(N):
        # 현재 칠하는 영역의 정보들
        info = list(map(int, input().split()))
        # 왼쪽 위 좌표
        r1, c1 = info[0], info[1]
        # 오른쪽 아래 좌표
        r2, c2 = info[2], info[3]
        # 칠할 색깔
        color = info[4]
        # 칠할 영역의 크키만큼 칠해야한다.
        # 세로 길이
        for i in range(r2-r1+1):
            # 가로 길이
            for j in range(c2-c1+1):
                # 만약 흰 종이라면 현재 칠할 색깔을 칠한다.
                if paper[r1+i][c1+j] == 0:
                    paper[r1 + i][c1 + j] = color
                # 흰색이 아니면
                else:
                    # 현재 색깔과 다른색이라면 보라색
                    if paper[r1+i][c1+j] != color:
                        paper[r1 + i][c1 + j] = 3
                    # 현재 색깔과 같은색이라면 유지
                    else:
                        continue
    # 각 행을 순회하면서 보라색의 개수를 찾는다.
    for k in range(10):
        result += paper[k].count(3)

    print(f'#{test_case}', result)


