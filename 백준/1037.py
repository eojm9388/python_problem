N = int(input())

num_list = list(map(int, input().split()))

A, B = max(num_list), min(num_list)

print(A * B)
