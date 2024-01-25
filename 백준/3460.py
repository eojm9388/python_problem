N = int(input())

for test_case in range(N):
    T = int(input())
    double_list = []

    while T > 0:
        double_list.append(T%2)
        T //= 2

    
    for i in range(len(double_list)):
        if double_list[i] == 1:
            print(i, end=' ')
    
    print()

