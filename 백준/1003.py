N = int(input())

for n in range(N):
    M = int(input())

    d = [[0, 0] for _ in range(M+1)]

    d[0] = [1, 0]
    if M >= 1:
        d[1] = [0, 1]

        for i in range(2, M+1):
            d[i] = [d[i-1][0] + d[i-2][0], d[i-1][1] + d[i-2][1]]


    print(d[M][0], d[M][1])
