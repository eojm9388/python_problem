for tc in range(1, 11):
    # 테이블의 한변의 크기 N -> 100으로 일정
    N = int(input())
    # 테이블에 놓인 자성들의 값 (위: N극, 아래: S극)
    table = [list(map(int, input().split())) for i in range(N)]
    # 전치행렬: 반시계로 90도 돌린 테이블 자성체 (왼: N극, 오른:S극)
    table_90 = [[table[j][i] for j in range(N)] for i in range(N)]

    # 교착 상태 개수
    cnt = 0
    # 왼쪽부터 자성체를 보면서 교착상태를 확인함
    for i in range(N):
        # 교착상태조건
        # 조건1: 왼쪽이 N극이기 때문에 상대적으로 왼쪽이 N극
        # 조건2: 조건 1을 만족 했을 때 S극 자성체가 나올 때 -> 상대적 오른쪽 S극

        # 교착상태가 아님
        deadlock = False
        for j in range(N):
            # 조건 2
            # 교착 상태이니 개수를 증가시키고 교착상태 초기화
            if deadlock and table_90[i][j] == 2:
                cnt += 1
                deadlock = False
            # 조건 1
            elif table_90[i][j] == 1:
                deadlock = True

    print(f'#{tc}', cnt)