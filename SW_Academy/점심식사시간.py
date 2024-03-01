from collections import deque

T = int(input())


# 완전 탐색 한다

# 함수 make_sequence
# 사람들이 각 계단을 선택하는 경우의 수를 stair_wait_people_1, stair_wait_people_2에 각각 담아주는 함수
# ex) 사람 3명 : 1번 사람, 2번 사람, 3번 사람
# 1번 계단: [1번 사람, 2번 사람, 3번 사람], [2번 사람, 3번 사람], [1번 사람, 3번 사람]... [아무도 없음]
# 2번 계단: [아무도 없음], [1번 사람], [2번 사람] ...[1번 사람, 2번 사람, 3번 사람]
# 이런 식으로 모든 경우에 걸리는 시간을 계산할거임
# 여기서는 사람 대신 그 계단까지 걸리는 시간을 넣을거임
def make_sequence():
    for i in range(1 << P):
        temp_1 = []
        temp_2 = []
        for j in range(P):
            # 1번 계단을 사용하는 사람이 1번 계단까지 이동하는데 걸리는 시간을 추가해준다
            if i & (1 << j):
                temp_1.append(people_move_time_1[j])
            # 2번 계단을 사용하는 사람이 2번 계단까지 이동하는데 걸리는 시간을 추가해준다
            else:
                temp_2.append(people_move_time_2[j])
        # 계단에 먼저 도착한 사람부터 계단을 이용해야하기 때문에 정렬 해준다
        # pop()을 사용할거기 때문에 reverse를 해준다
        temp_1.sort(reverse=True)
        temp_2.sort(reverse=True)
        # stair_wait_people_N: N번 계단에 대기중인 사람 -> 인덱스: 인덱스번째 경우의 수, 값: N번 계단에 대기중인 사람(실제값: N번 계단까지 이동하는 걸린 시간)
        stair_wait_people_1.append(temp_1)
        stair_wait_people_2.append(temp_2)


# 계단을 사용할 때 걸리는 시간을 반환해주는 함수 (계단을 내려가는데 걸리는 시간, 계단에 대기중이 사람)
def cal_time(stair_number, stair_person):
    # 만약 대기중인 사람이 3명 이하면 3명 동시에 이용가능 -> 맨 마지막에 도착한 사람이 계단을 사용하고 난 뒤 시간
    if len(stair_person) <= 3:
        if stair_person:
            return stair_person[0] + stair_number + 1
        # 아무도 계단을 사용하지 않는다면 0분
        else:
            return 0
    # 계단을 사용하는 사람이 3명 이상일 경우
    else:
        # 밑에 코드가 실행되는 과정의 예시
        # ex) 1번 계단을 내려가는데 걸리는 시간 3, 현재 1번 계단을 사용할 사람 5명, 1번 계단까지 도착한 시간 [5, 5, 3, 2, 2]

        # 현재 계단을 사용하는 사람의 남은 시간
        stair_inner = []
        # wait_time: 계단을 모두 내려가는데 걸린 시간
        # 처음 계단을 내려갈때는 맨 먼저 도착한 사람의 시간 -> 2
        wait_time = stair_person.pop()
        # 첫번째 사람이 계단을 내려감 [T]
        stair_inner.append(stair_number)

        # 모든 사람이 계단을 다 내려갈 때까지 반복
        while stair_person:
            # 조건: 계단은 최대 3명까지 사용 가능, 계단을 사용할 사람이 있으면, 계단위에서 대기중인 사람이 있다면
            # 시간 - 2분 : 계단 1명 사용 중, 계단에 도착할 사람 남았음, 2분에 계단에 도착한 사람 1명 있음
            # 시간 - 3분 : 계단 2명 사용 중, 계단에 도착할 사람 남았음, 3분에 계단에 도착한 사람 1명 있음
            # 시간 - 4분 : 계단 3명 사용 중, 계단에 도착할 사람 남았음, 4분에 계단에 도착한 사람 없음
            # 시간 - 5분 : 계단 1명 사용 중, 계단에 도착할 사람 남았음, 5분에 계단에 도착한 사람 2명 있음
            # 시간 - 6분 : 계단 2명 사용 중, 계단에 도착할 사람 없음
            while len(stair_inner) < 3 and stair_person and wait_time >= stair_person[-1]:
                # 계단을 사용할 수 있는 사람이 있으면 계단에 넣어주기
                if stair_person:
                    # 시간 - 2분: 2분에 도착한 사람 1명 더 계단 사용, 계단 [3, 3]
                    # 시간 - 3분: 3분에 도착한 사람 1명 더 계단 사용, 계단 [2, 2, 3]
                    # 시간 - 4분: 4분에 도착한 없음, 계단 [1, 1, 2]
                    # 시간 - 5분: 5분에 도착한 사람 2명 더 계단 사용, 계단 [1, 3, 3]
                    stair_person.pop()
                    stair_inner.append(stair_number)
                # 계단을 사용할 있는 사람이 없다면 다음으로
                else:
                    break

            # 계단을 사용할 사람이 다 정해짐
            # 계단 1분 사용

            # 시간 - 2분: [2, 2]
            # 시간 - 3분: [1, 1, 2]
            # 시간 - 4분: [0, 0, 1]
            # 시간 - 5분: [0, 2, 2]

            for w in range(len(stair_inner)):
                stair_inner[w] -= 1
            # 다 내려간 사람들을 빼는 작업

            # 시간 - 2분: 아직 계단을 내려가는 중 [2, 2]
            # 시간 - 3분: 아직 계단을 내려가는 중 [1, 1, 2]
            # 시간 - 4분: 2명이 계단을 다 내려감 [1]
            # 시간 - 5분: 1명이 계단을 다 내려감 [2, 2]
            if stair_inner and stair_inner[0] == 0:
                for _ in range(len(stair_inner)):
                    if stair_inner and stair_inner[0] == 0:
                        stair_inner.pop(0)
                    else:
                        break
            # 시간 증가
            wait_time += 1

        # 계단 대기인원이 없다면 계단안에 있는 마지막 사람의 시간만 더해주면 된다

        # 시간 - 6분일 때 계단을 사용할 사람이 없음, 계단 [2, 2]
        # 하지만 계단 맨 위에 있는 사람이 다 내려오는데 2분이 더 걸림
        # 근데 여기서 1분을 더 더해야함 -> 이유를 알듯말듯...

        wait_time += stair_inner[-1]

        return wait_time + 1


for tc in range(1, T + 1):
    N = int(input())

    MAP = [list(map(int, input().split())) for _ in range(N)]
    # 사람들의 위치 좌표
    people = []
    # 계단들의 위치 좌표
    stair = []

    stair_wait_people_1 = []
    stair_wait_people_2 = []

    # 사람들과 계단의 좌표를 구해준다
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 1:
                people.append([i, j])
            # 계단은 계단의 높이까지 더해줌
            elif MAP[i][j] > 1:
                stair.append([i, j, MAP[i][j]])

    # 사람들의 숫자
    P = len(people)
    # 1번 계단의 좌표
    stair_1 = stair[0]
    # 2번 계단의 좌표
    stair_2 = stair[1]
    # 모든 사람이 1번 계단까지 가는데 걸리는 시간
    people_move_time_1 = []
    # 모든 사람이 2번 계단까지 가는데 걸리는 시간
    people_move_time_2 = []

    # 계단까지 걸리는 시간 계산
    for person in people:
        move_time_1 = abs(stair_1[0] - person[0]) + abs(stair_1[1] - person[1])
        move_time_2 = abs(stair_2[0] - person[0]) + abs(stair_2[1] - person[1])
        people_move_time_1.append(move_time_1)
        people_move_time_2.append(move_time_2)

    # 사람들이 계단을 사용하는 모든 경우의 수를 만들어준다
    make_sequence()
    # 모든 경우의 수의 개수
    C = len(stair_wait_people_1)

    # 최소 걸린 시간
    min_time = 1000
    for case in range(C):
        # case번 경우에서 해당 계단을 사용할 때 걸리는 시간
        time_1 = cal_time(stair_1[2], stair_wait_people_1[case])
        time_2 = cal_time(stair_2[2], stair_wait_people_2[case])
        # print(max(time_1, time_2))
        # 두 시간 중에 더 큰 시간이 모든 사람이 다 내려온 시간이다.
        # 최소 시간 갱신

        if min_time > max(time_1, time_2):
            # print(case)
            min_time = max(time_1, time_2)

        # cal_time 에 최솟값을 가지치기 하여 더 줄일 수 있을거 같음 -> 보완 필요

    print(f'#{tc}', min_time)