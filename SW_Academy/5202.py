T = int(input())

for tc in range(1, T+1):
    # 신청서 개수 N
    N = int(input())
    # 화물차의 작업시간 [s, e]를 담은 리스트
    time = [list(map(int, input().split())) for _ in range(N)]
    # 화물차 작업시간 정렬 -> 시작 시간이 같더라도 종료시간이 작은 순으로 정렬된다
    time.sort()
    # 작업할 수 있는 화물차 개수
    cnt = 1
    # 처음 작업 시간 할당
    start, end = time[0][0], time[0][1]

    for s, e in time[1:]:
        # 만약 작업 종료 시간이 뒤에 신청서가 더 작다면 갱신
        # ex) start:2 end:15 s:5 e:12 라면 갱신
        if e < end:
            start, end = s, e
        # 다음 신청서의 시작 시간이 현재 신청서의 종료시간 이상이라면
        # 작업할 수 있는 화물차 개수를 증가시키고 작업시간 갱신
        elif end <= s:
            cnt += 1
            start, end = s, e


    print(f'#{tc}', cnt)
