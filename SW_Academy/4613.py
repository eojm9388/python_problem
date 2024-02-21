T = int(input())

for tc in range(1, T+1):
    # N행 M열 깃발
    N, M = map(int, input().split())
    # 깃발에 칠해진 색깔 2차원 리스트
    flag = [list(input()) for _ in range(N)]

    # 각 줄에 하얀색이 몇 칸 있는지
    white = [0] * N
    # 각 줄에 파란색이 몇 칸 있는지
    blue = [0] * N
    # 각 줄에 빨간색이 몇 칸 있는지
    red = [0] * N
    # 각 경우마다 몇개의 색깔을 바꿔야하는지
    result = []
    # 각 줄 마다 각 색깔을 칠할 경우 몇칸을 칠해야 하는지
    for i in range(N):
        white[i] = M - flag[i].count('W')
        blue[i] = M - flag[i].count('B')
        red[i] = M - flag[i].count('R')
    # tc1) white = [2, 3, 2, 3]
    # 1번째 줄을 하얀색으로 칠할려면 2칸
    # 2번째 줄 3칸, 3번째 줄 2칸, 4번째 줄 3칸을 칠해야함
    # print(white)

    # 깃발을 만들 수 있는 모든 경우의 수를 구한다
    # tc1) N = 4
    # 1) W  2) W  3) W   -> W를 칠할 줄의 개수와
    #    B     B     W      B를 칠할 줄의 개수가
    #    R     B     B      정해지면 R을 칠할 줄의 개수도
    #    R     R     R      정해진다.
    for w in range(N-2):
        for b in range(w+1, N-1):
            count = 0
            count += sum(white[:w+1])
            count += sum(blue[w+1:b+1])
            count += sum(red[b+1:])
            result.append(count)
    # 제일 적게 칠하는 칸의 개수를 출력한다.
    print(f'#{tc}', min(result))



