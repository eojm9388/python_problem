N = input()
M = int(input())
if M > 0:
    no_arr = list(map(int, input().split()))
    arr = [str(x) for x in range(10) if x not in no_arr]
else:
    arr = list(map(str, range(10)))


min_cnt = abs(int(N) - 100)

for i in range(1000001):
    make = True
    temp = str(i)

    for j in temp:
        if j not in arr:
            make = False
            break

    if make:
        min_cnt = min(min_cnt, abs(i-int(N))+len(temp))


print(min_cnt)




