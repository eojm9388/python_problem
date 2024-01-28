A, B = map(int, input().split())

A_num1, B_num1 = A, B
num_list = []
num = 2 

while True:
    if A_num1 % num == 0 and B_num1 % num == 0:
        num_list.append(num)
        A_num1 //= num
        B_num1 //= num
        num = 2
    else:
        num += 1
    
    if A_num1 < num or B_num1 < num:
        break

num_1 = 1

for n in num_list:
    num_1 *= n
print(num_1)

num_A, num_B = 1, 1

while True:
    A_num2 , B_num2 = A, B
    if A_num2 * num_A > B_num2 * num_B:
        B_num2 *= num_B
        num_B += 1

    elif A_num2 * num_A < B_num2 * num_B:
        A_num2 *= num_A
        num_A += 1
    
    else:
        break

print(A_num2 * num_A)