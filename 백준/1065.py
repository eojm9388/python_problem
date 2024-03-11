N = int(input())

def f(n):
    temp = str(n)
    if len(temp) >= 2:
        A = int(temp[0])
        B = int(temp[1])
        C = B - A
        A = B
        for i in temp[2:]:
            B = int(i)
            temp2 = B - A
            if C != temp2:
                return False
            else:
                A = B
        return True
    else:
        return True


cnt = 0
for i in range(1, N+1):
    if f(i):
        cnt += 1

print(cnt)