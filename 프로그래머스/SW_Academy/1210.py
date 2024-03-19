import sys
sys.stdin = open("input.txt", "r")

for t in range(1, 11):
    test_case = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]
    result = 0


    for start in range(100):
        # 출발지점의 행 번호
        i = 0
        # 출발지점의 열 번호
        j = start
        # 움직일 방향 0:아래, 1:오른쪽, 2:왼쪽
        direction = 0
        # 만약 출발지점이 1이라면 출발! 0이라면 시작부분에 사다리가 없는거임
        if ladder[i][j] == 1:
            # 아래로 99번 움직이면 도착지점이기 때문에
            while i < 99:
                # 만약 현재 방향이 아래라면
                if direction == 0:
                    # 밑으로 한칸
                    i += 1
                    # print('아래로 한칸')
                    # 제일 왼쪽이라면 사다리의 오른쪽만 다리가 있다
                    if j == 0:
                        # 만약 오른쪽에 다리가 있다면 방향을 오른쪽으로 바꾼다.
                        if ladder[i][j+1] == 1:
                            direction = 1
                    # 제일 오른쪽이라면 사다리의 왼쪽에만 다리가 있다
                    elif j == 99:
                        # 만약 왼쪽에 다리가 있다면 방향을 왼쪽으로 바꾼다.
                        if ladder[i][j-1] == 1:
                            direction = 2
                    # 사다리 중앙?에 있다면 양쪽에 다리가 있을 수 있다.
                    else:
                        # 만약 오른쪽에 다리가 있다면 방향을 오른쪽으로 바꾼다.
                        if ladder[i][j+1] == 1:
                            direction = 1
                        # 만약 왼쪽에 다리가 있다면 방향을 왼쪽으로 바꾼다.
                        elif ladder[i][j-1] == 1:
                            direction = 2
                # 만약 현재 방향이 오른쪽이라면
                elif direction == 1:
                    # 오른쪽으로 한칸
                    j += 1
                    # print('오른쪽으로 한칸')
                    # 이동 후 만약 아래쪽에 사다리가 있다면 방향을 아래로 바꾼다.
                    if ladder[i+1][j] == 1:
                        direction = 0
                # 만약 현재 방향이 왼쪽이라면
                elif direction == 2:
                    j -= 1
                    # print('왼쪽으로 한칸')
                    # 이동 후 만약 아래쪽에 사다리가 있다면 방향을 아래로 바꾼다.
                    if ladder[i+1][j] == 1:
                        direction = 0
            # while문을 빠져나온뒤
            # 도착지점이 2라면 출발지점을 결과에 넣는다.
            if ladder[i][j] == 2:
                result = start
                break

    print(f'#{test_case}', result)


