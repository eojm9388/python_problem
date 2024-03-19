T = int(input())

for tc in range(1, T+1):
    # 농장의 크기
    N = int(input())
    # 농장 2차원 리스트
    field = [list(map(int, input())) for _ in range(N)]
    # 수익
    result = 0
    # print(field)


    # 각 줄의 양 옆에 수확하지 못하는 농작물의 칸의 개수
    line_count = N // 2
    # n번째 줄
    line_num = 0
    # 수확할 수 있는 농작물 개수 구하기
    # tc1) 1번째 줄 = 5번째 줄 = -2  5  -2 = 1칸
    #      2번째 줄 = 4번째 줄 = -1  5  -1 = 3칸
    #      3번째 줄 = 0  5  0 = 5칸
    while line_count > 0:
        result += sum(field[line_num][line_count:N-line_count])
        result += sum(field[-(line_num+1)][line_count:N-line_count])
        # print(field[line_num][line_count:N-line_count])
        # print(field[-(line_num+1)][line_count:N-line_count])
        line_num += 1
        line_count -= 1

    result += sum(field[line_num])

    print(f'#{tc}', result)