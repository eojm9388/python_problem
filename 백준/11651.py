T = int(input())

dot_list = []

for test_case in range(T):
    x, y = map(int, input().split())

    dot_list.append([y, x])

dot_list.sort()

for y, x in dot_list:
    print(x, y)