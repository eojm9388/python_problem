def f(n, s):
    if s == 6:
        print(*temp)
        return
    if n >= k:
        return
    temp.append(S[n])
    f(n+1, s+1)
    temp.pop()
    f(n+1, s)



while True:
    line = list(map(int, input().split()))

    if line[0] == 0:
        break
    else:
        k = line[0]
        S = line[1:]
        temp = []
        f(0, 0)
        print()
