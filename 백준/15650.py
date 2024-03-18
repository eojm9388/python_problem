N, M = map(int, input().split())


# 순열을 만드는 함수
def f(i):
    # M개의 숫자만 고른다
    if i == M:
        temp_2 = temp[:]
        # 오름차순 정렬
        temp_2.sort()
        # 중복 제거
        if temp_2 not in result:
            result.append(temp_2)
        return

    # 중복 없는 순열
    for j in range(0, N):
        if used[j] == 0:
            used[j] = 1
            temp.append(j + 1)
            f(i + 1)
            temp.pop()
            used[j] = 0


used = [0] * N
temp = []
result = []
f(0)
# 차례대로 출력
for r in result:
    print(*r)