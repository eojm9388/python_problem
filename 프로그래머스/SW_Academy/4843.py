import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# 버블 정렬
def bubble_sort(arr, option):
    lenght = len(arr)
    if option == True:
        for i in range(lenght):
            for j in range(1, lenght):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
        return arr
    elif option == False:
        for i in range(lenght):
            for j in range(1, lenght):
                if arr[j] > arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
        return arr
# 카운팅 정렬
def counting_sort(arr, option):
    lenght = len(arr)
    max_num = max(arr)
    counts = [0] * (max_num+1)
    for i in arr:
        counts[i] += 1

    for j in range(1, max_num + 1):
        counts[j] += counts[j - 1]
    temp = [0] * lenght
    if option:
        for k in arr:
            temp[counts[k]-1] = k
            counts[k] -= 1

    else:
        for k in arr:
            temp[lenght-counts[k]] = k
            counts[k] -= 1

    return temp
# 선택 정렬
def selection_sort(arr, option):
    lenght = len(arr)
    if option:
        for i in range(lenght):
            min_num = min(arr[i:])
            min_num_index = arr.index(min_num)
            arr[i], arr[min_num_index] = arr[min_num_index], arr[i]
    else:
        for i in range(lenght):
            max_num = max(arr[i:])
            max_num_index = arr.index(max_num)
            arr[i], arr[max_num_index] = arr[max_num_index], arr[i]

    return arr


for test_case in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    # 오름차순 - 버블 정렬
    asc_num_list = bubble_sort(num_list, True)
    # 내림차순 - 카운팅 정렬
    des_num_list = counting_sort(num_list, False)
    # 결과값
    result = []

    for t in range(5):
        # 큰 수 하나, 작은 수 하나씩 넣기
        result.append(des_num_list[t])
        result.append(asc_num_list[t])

    print(f'#{test_case}', *result)
