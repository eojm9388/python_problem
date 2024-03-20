N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]
arr.sort(reverse=True)
# print(arr)
cnt = 0
difference = []
same = []

while arr:
    line_1 = arr[0]

    for j in range(1, len(arr)):
        line_2 = arr[j]
        for k in range(M):
            if line_1[k] == '.' or line_2[k] == '.':
                continue
            else:
                if line_1[k] != line_2[k]:
                    break
        else:
            same.append(j)
    print(same)
    while same:
        t = same.pop()
        arr.pop(t)

    cnt += 1
    arr.pop(0)
    # print(arr)

print(cnt)
