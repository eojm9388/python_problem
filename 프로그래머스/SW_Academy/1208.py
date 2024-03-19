for test_case in range(1, 11):
    dunp_count = int(input()) # 덤프 가능 횟수
    box_height = list(map(int, input().split())) # 박스들의 높이 리스트

    counts = [0] * 101                    # 박스 높이별로 개수를 구할 리스트

    for i in box_height:
        counts[i] += 1                    # 박스의 높이별로 개수 증가

    j = 0                                 # 현재 덤프를 한 횟수
    start = 1                             # 가장 낮은 박스의 높이

    while j < dunp_count:                 # 높이가 낮은 박스들을 덤프로 증가시키는 반복문
        if counts[start] > 0:             # 만약 가장 낮은 높이의 박스를 찾았다면
            counts[start] -= 1            # 박스 하나를 추가하여 높이를 1 증가
            counts[start+1] += 1
            j += 1                        # 현재 덤프 횟수 추가
            if counts[start] > 0:         # 현재 가장 낮은 높이의 박스가 남아 있다면
                continue                  # 다시 순회
        start += 1                        # 없다면 높이 1 증가

    j = 0                                 # 현재 덤프를 한 횟수
    end = 100                             # 가장 높은 박스의 높이

    while j < dunp_count:                 # 높이가 높은 박스들을 덤프로 감소시키는 반복문
        if counts[end] > 0:               # 만약 가장 높은 높이의 박스를 찾았다면
            counts[end] -= 1              # 박스 하나를 감소하여 높이를 1 감소
            counts[end-1] += 1
            j += 1                        # 현재 덤프 횟수 추가
            if counts[end] > 0:           # 만약 가장 높은 높이의 박스가 남았다면
                continue                  # 다시 순회
        end -= 1                          # 없다면 높이 1 감소

    print(f'#{test_case} {end - start}')  # 덤프를 모두 수행한 후 최고높이와 최저높이의 차

