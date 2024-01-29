for test_case in range(1, 11):
    N = int(input()) # 빌딩의 개수
    building_list = list(map(int, input().split())) # 빌딩의 높이 리스트
    right_of_view_count = 0 # 조망권이 확보된 세대의 수
    for i in range(2, N-2): # 빌딩 리스트에서 양쪽 두칸은 모두 0이기 때문에 2부터 N-2까지 반복 
        right_of_view = True # 조망권이 확보되었다고 가정
        max_building = 0 # 양옆 두 빌딩 중 제일 높은 빌딩높이
        
        for j in range(i-2, i+3): # 해당 인덱스로부터 양쪽 2만큼 떨어진 곳을 순회
            if j == i: # 자기 자신은 패스
                continue
            if building_list[i] < building_list[j]: # 만약 양쪽에서 한 빌딩이라도 높다면 조망권 확보실패
                right_of_view = False               # 따라서 False로 바꾸고 반복문 탈출
                break
            if max_building < building_list[j]:     # 양옆 중 제일 높은 빌딩을 구해야한다.
                max_building = building_list[j]
        if right_of_view: # 양 옆을 다 보았는데 조망권이 확보 되었다면 
            plus_count = building_list[i] - max_building # 현재 빌딩의 높이 - 양옆중 가장 높은 빌딩의 높이
            right_of_view_count += plus_count            # = 조망권이 확보된 세대의 수
    print(f'#{test_case} {right_of_view_count}')
