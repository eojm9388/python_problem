T = int(input())

# path_list에 관리구역을 가는 경로의 경우의 수를 추가해주는 함수
def path_search(i, k):
    if i == k:
        # 이때까지 기록한 경로
        temp = path[:]
        path_list.append(temp)
        return
    # 2번부터 관리구역이다
    for j in range(2, N+1):
        # 전에 사용하지 않았던 경로라면
        if path_used[j] == 0:
            # 경로 추가
            path_used[j] = 1
            path.append(j)
            # 다음 경로 찾기
            path_search(i+1, k)
            # 함수 복귀 후 초기화
            path_used[j] = 0
            path.pop()



for tc in range(1, T+1):
    N = int(input())
    # 이동시 배터리 사용량
    battery = [list(map(int, input().split())) for _ in range(N)]
    # 각 구역을 가는 경우의 수 -> 순열
    # path -> 관리 구역을 가는 경로
    path = []
    # 여러개의 path를 담은 리스트
    path_list = []
    # 지나간 경로를 중복시키지 않기 위해 사용
    path_used = [0] * (N+1)
    # 사무실을 제외한 관리구역을 가는 경로
    path_search(0, N-1)
    # 결과값 리스트
    result_list = []

    # 배터리 사용량 구하기
    # turn = path -> 관리구역을 가는 경로
    for turn in path_list:
        # 사무실에서 첫번째 관리구역으로 갈 때 배터리 사용
        result = battery[0][turn[0]-1]
        # 관리구역에서 다음 관리구역으로 갈 때 배터리 사용
        for i in range(1, len(turn)):
            result += battery[turn[i-1]-1][turn[i]-1]

        # 마지막 관리구역에서 사무실로 돌아올 때 배터리 사용
        result += battery[turn[-1]-1][0]
        # 결과값 추가
        result_list.append(result)

    # 최솟값 출력
    print(f'#{tc}', min(result_list))


