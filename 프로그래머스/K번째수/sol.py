def counting_sort(arr, option):
    max_arr = max(arr)
    N = len(arr)
    
    counts = [0] * (max_arr+1)
    for i in arr:
        counts[i] += 1
        
    for j in range(1, max_arr+1):
        counts[j] += counts[j-1]
    
    temp = [0] * N
    if option:
        for k in arr:
            temp[counts[k]-1] = k
            counts[k] -= 1
    else:
        for k in arr:
            temp[N-counts[k]] = k
            counts[k] -= 1
    return temp
    
def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command[0], command[1], command[2] 
        arr = array[i-1:j]
        print(arr)
        arr_sort = counting_sort(arr, True)
        answer.append(arr_sort[k-1])
        
    return answer
    