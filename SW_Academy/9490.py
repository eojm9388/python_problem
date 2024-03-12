T = int(input())

def flower_count(x, y, N, M):         # 꽃가루의 총합의 구하는 함수
    r = balloon[x][y]                 # 풍선이 터지는 범위
    result = 0                        # 꽃가루 총합
    for i in range(-r, r+1):          # 세로방향으로 터지는 풍선
        if x + i < 0 or x + i >= N:   # 만약 줄을 벗어난다면 스킵
            continue
        else:
            result += balloon[x+i][y] # 아니라면 풍선에 담긴 꽃가루 더하기

    for j in range(-r, r+1):          # 가로방향으로 터지는 풍선
        if y+j < 0 or y+j >= M:       
            continue
        else:
            result += balloon[x][y+j] 

    result -= r                       # 가로 한번, 세로 한번 터지기 때문에
                                      # 중앙이 한번 더 더해지기 때문에 
                                      # 가운데 꽃가루 한번 빼주기
    return result



for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    max_result = 0                  # 최대 꽃가루 총합

    balloon = [list(map(int, input().split())) for i in range(N)]    # 풍선 배열
    for x in range(N):  
        for y in range(M):
            result = flower_count(x, y, N, M)    # 풍선 배열을 모두 돌아 최대 꽃가루 총합을 구한다.
            if result > max_result:
                max_result = result
    print(f'#{test_case}', max_result)
