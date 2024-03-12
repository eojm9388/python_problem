A, B, V = map(int, input().split())




one_day_height = A - B # 하루에 목표높이까지 도달하지 못하면 올라갈 수 있는 높이
yesterday_height = V - A # 목표에 도달하기 하루 전 목표 높이
if yesterday_height % one_day_height > 0: 
    # 연산자 //은 정수 나눗셈으로 내림을 하기 때문에
    # 문제에서는 올림을 해야한다.
    # 따라서 나머지가 1 이상이라면 하루가 더 추가되야한다.
    # math라이브러리에 .ceil 메서드를 사용하여도 된다.
    day = yesterday_height // one_day_height + 2  # 달팽이가 목표 높이까지 올라가는데 걸리는 일
else:
    day = yesterday_height // one_day_height + 1




# 목표에 도달하기 하루 전까지는 매일 올라갔다 떨어졌다를 반복
# 전날 목표 높이에서 하루동안 올라가는 높이를 나눠주면 전날까지 걸린 일수가 나옴
# 그 일수에 1만 더해주면 목표 높이까지 올라가는데 걸린 일수가 됨


# Test case 3번이 너무 오래 걸림
# while True: 
#     day += 1
#     height += A # 낮에 올라가는 높이
#     if height >= V: # 만약 목표 높이에 도달 했다면 반복문 탈출
#         break
#     height -= B # 밤에 떨어지는 높이
#     print(height)

print(day)

