<<<<<<< HEAD
from itertools import permutations
=======
>>>>>>> 0d62b852ccfd592f56f7fc231cb52cab4247e6b0
N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]
arr.sort(reverse=True)
<<<<<<< HEAD

cnt_list = []
same = []

for new in permutations(arr):
    cnt = 0
    new = list(new)
    while new:
        line_1 = new[0]

        for j in range(1, len(new)):
            line_2 = new[j]
            for k in range(M):
                if line_1[k] == '.' or line_2[k] == '.':
                    continue
                else:
                    if line_1[k] != line_2[k]:
                        break
            else:
                same.append(j)
        while same:
            t = same.pop()
            new.pop(t)

        cnt += 1
        new.pop(0)
    cnt_list.append(cnt)

print(max(cnt_list))
=======
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
>>>>>>> 0d62b852ccfd592f56f7fc231cb52cab4247e6b0
