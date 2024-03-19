T = int(input())

for tc in range(1, T+1):
    # 컨테이너 개수 N, 트럭 수 M
    N, M = map(int, input().split())
    # 컨테이너 무게
    weight = list(map(int, input().split()))
    # 트럭의 적재용량
    truck = list(map(int, input().split()))
    # 컨테이너 무게와 트럭의 적재용량 정렬
    weight.sort()
    truck.sort()
    # 옮길 수 있는 최대 무게
    total = 0
    # 무거운 것부터 옮긴다
    # 가벼운 것부터 옮기지 않는 이유 -> 더 무거운 것을 옮길 수 있는 트럭을 사용해버릴 수 있기 때문에
    # ex) 컨테이너 무게: [1, 5, 7] , 트럭 적재용량: [5, 7]
    # 이 경우 가벼운 것을 먼저하면 1을 옮기기 위해 적재용량이 5인 트럭을 사용해야한다

    # 트럭이 옮길 수 있는 무게와 비교할 컨테이너 무게의 인덱스
    # 리스트의 마지막부터 인덱스할 것이기 때문에 1부터
    idx = 1
    # 종료조건1: 트럭을 다 사용하였다
    while truck:
        # 남은 트럭 중 적재용량이 제일 큰 트럭
        ok_w = truck.pop()

        # 남은 컨테이너 중 제일 무거운 컨테이너를 옮긴다
        while True:
            if weight[-idx] <= ok_w:
                total += weight[-idx]
                # 다음 트럭은 현재 컨테이너보다 가벼운 것들만 옮길 수 있다.
                idx += 1
                break
            # 만약 현재 트럭이 옮기지 못하는 무게면 다음 가벼운 컨테이너 무게를 탐색
            idx += 1
            # 더 이상 옮길 수 있는 컨테이너가 없다면 종료
            if idx > N:
                break
        # 종료조건2: 트럭이 남아있더라도 옮길 수 있는 컨테이너가 없는 경우
        if idx > N:
            break

    print(f'#{tc}', total)