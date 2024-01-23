T = int(input())

dot_list = []

for test_case in range(T):
    dot = list(map(int, input().split()))
    dot_list.append(dot)

dot_list.sort()

for x, y in dot_list:
    print(x, y)
