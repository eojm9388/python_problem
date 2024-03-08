N = int(input())


def f(n, start, end, temp):
    global cnt
    cnt += 1
    if n == 1:
        result.append([start, end])
        return

    f(n-1, start, temp, end)
    result.append([start, end])
    f(n-1, temp, end, start)

cnt = 0
result = []
f(N, 1, 3, 2)
print(cnt)
for i in range(cnt):
    print(*result[i])
