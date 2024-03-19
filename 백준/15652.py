N, M = map(int, input().split())

def f(i):
    if i == M:
        print(*temp)
        return

    for j in range(1, N+1):
        if temp == [] or j >= temp[-1]:
            temp.append(j)
            f(i+1)
            temp.pop()

temp = []

f(0)