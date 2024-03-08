from collections import deque
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    op_cnt_list = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    numbers_sort = sorted(numbers)
    print(numbers_sort)


def max_num():
    result = numbers[0]
    n = 1
    while n < N:
        for i in range(N):
            if numbers[n] 
