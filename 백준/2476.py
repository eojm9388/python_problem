T = int(input())

money_list = []

for test_case in range(T):
    result = 0
    dice_a, dice_b, dice_c = map(int, input().split())
    
    if dice_a == dice_b == dice_c:
        result = 10000 + dice_a * 1000 
    elif dice_a == dice_b:
        result = 1000 + dice_a * 100
    elif dice_a == dice_c:
        result = 1000 + dice_a * 100
    elif dice_b == dice_c:
        result = 1000 + dice_b * 100
    else:
        result = max(dice_a, dice_b, dice_c) * 100
    
    money_list.append(result)

print(max(money_list))
    
