T = int(input())

for test_case in range(T):
    A, B = map(int, input().split())

    num_A, num_B = 1, 1

    while A * num_A != B * num_B:
        if A * num_A > B * num_B:
            num_B += 1

        else: 
            num_A += 1
        

    print(A * num_A)