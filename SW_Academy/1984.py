T = int(input())

for test_case in range(1, T + 1):
    num_list = list(map(int, input().split()))
    max_num = max(num_list)
    min_num = min(num_list)

    num_list.remove(max_num)
    num_list.remove(min_num)

    result = int(round(sum(num_list) / len(num_list), 0))
    
    print(f'#{test_case} {result}')
