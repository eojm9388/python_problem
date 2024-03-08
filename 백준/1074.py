N, r, c = map(int, input().split())


def f(i, j, n):
    if n == 0:
        return 0

    half = 2**n//2

    if i >= half and j >= half:
        return 3*half*half + f(i-half, j-half, n-1)

    elif i >= half and j < half:
        return 2*half*half + f(i-half, j, n-1)

    elif i < half and j >= half:
        return half*half + f(i, j-half, n-1)

    else:
        return f(i, j, n-1)


print(f(r, c, N))