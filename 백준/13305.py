N = int(input())

distance = list(map(int, input().split()))

cost_L = list(map(int, input().split()))

idx = 0
money = 0
current_idx = 1
sum_dis = 0
while idx < N-1 and current_idx < N:
    sum_dis += distance[current_idx - 1]
    if cost_L[idx] < cost_L[current_idx]:
        current_idx += 1
    else:
        money += cost_L[idx] * sum_dis
        sum_dis = 0
        idx = current_idx
        current_idx += 1

print(money)