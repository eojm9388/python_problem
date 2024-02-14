# import sys
# sys.stdin = open('input.txt')

T = int(input())

# 배열 최소 합을 구하는 함수
def f(i, k, s):
    # 최소 합
    global min_sum
    # global cnt
    # cnt += 1
    if i == k:
        if min_sum > s:
            min_sum = s

    elif s >= min_sum:
        return

    else:
        for j in range(i, k):
            P[i], P[j] = P[j], P[i]
            f(i+1, k, s+array[i][P[i]])
            P[i], P[j] = P[j], P[i]

for tc in range(1, T+1):
    N = int(input())

    array = [list(map(int, input().split())) for _ in range(N)]
    P = list(range(N))
    min_sum = 100
    # cnt = 0
    f(0, N, 0)
    # print(min_sum, cnt)
    print(f'#{tc}', min_sum)