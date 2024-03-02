from collections import deque
T = int(input())

def f(i, k):
    if i == k:
        if op_case not in op_case_list:
            temp = op_case[:]
            op_case_list.append(temp)
        return

    for j in range(C):
        if used[j] == 0:
            used[j] = 1
            op_case.append(op[j])
            f(i+1, k)
            used[j] = 0
            op_case.pop()

def cal(arr):
    # print(arr)
    cal_result = arr[0]
    for n in range(1, len(arr), 2):
        if arr[n] == '+':
            cal_result += arr[n+1]
        elif arr[n] == '-':
            cal_result -= arr[n+1]
        elif arr[n] == '*':
            cal_result *= arr[n+1]
        elif arr[n] == '/':
            if cal_result < 0 and abs(cal_result) < arr[n+1]:
                cal_result = 0
            else:
                cal_result //= arr[n+1]


    return cal_result
for tc in range(1, T+1):
    # 숫자의 개수 N, K번째 큰수
    N = int(input())
    op_cnt_list = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    op = []
    for i in range(4):
        op_cnt = op_cnt_list[i]
        for _ in range(op_cnt):
            if i == 0:
                op.append('+')
            elif i == 1:
                op.append('-')
            elif i == 2:
                op.append('*')
            elif i == 3:
                op.append('/')

    C = len(op)
    op_case_list = []
    op_case = []
    used = [0] * C
    f(0, C)
    calculation_list = []
    print(calculation_list)

    # for op_case in op_case_list:
    #     calculation = []
    #     numbers_q = deque(numbers)
    #     for i in range(C):
    #         calculation.append(numbers_q.popleft())
    #         calculation.append(op_case.pop())
    #
    #     calculation.append(numbers_q.popleft())
    #     calculation_list.append(calculation)
    #
    # # print(calculation_list)
    # result_list = []
    #
    # for calculation in calculation_list:
    #     result = cal(calculation)
    #     result_list.append(result)
    #
    # print(f'#{tc}', max(result_list) - min(result_list))