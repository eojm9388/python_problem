N = int(input())

dice = []
result_list = []
for i in range(N):
    line = list(map(int, input().split()))
    # [A F, B D, C E] 순으로 저장 -> 맞은편 숫자들
    temp_1 = [line[0], line[5], line[1], line[3], line[2], line[4]]
    dice.append(temp_1)


for j in range(1, 7):
    # 한면의 숫자합
    result = 0
    # 1을 제일 밑의 주사위의 아랫면 숫자 -> 이게 정해지면 다른 주사위들의 윗면과 아랫면이 정해짐
    num1 = j
    for k in range(N):
        # num1 = 주사위의 아랫면 숫자
        # num2 = 주사위의 윗면 숫자
        # 주사위의 아랫면 숫자가 있는 인덱스
        num1_idx = dice[k].index(num1)
        # num1_idx가 짝수면 반대쪽 숫자의 인덱스는 1을 더한거

        # 윗면가 아랫면을 숫자를 리스트의 맨뒤로 보낸다
        if num1_idx % 2 == 0:
            num2 = dice[k][num1_idx+1]
            num2_idx = dice[k].index(num2)
            dice[k][4], dice[k][num1_idx] = dice[k][num1_idx], dice[k][4]
            dice[k][5], dice[k][num2_idx] = dice[k][num2_idx], dice[k][5]
        # num1_idx가 홀수면 반대쪽 숫자의 인덱스는 1을 뺀거
        elif num1_idx % 2 == 1:
            num2 = dice[k][num1_idx-1]
            num2_idx = dice[k].index(num2)
            dice[k][4], dice[k][num2_idx] = dice[k][num2_idx], dice[k][4]
            dice[k][5], dice[k][num1_idx] = dice[k][num1_idx], dice[k][5]
        # 윗면 숫자 갱신
       num1 = num2
        # 나머지 면들 중 제일 큰 숫자 더하기
        result += max(dice[k][:4])

    result_list.append(result)

print(max(result_list))




