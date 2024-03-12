S = int(input())

num = 1
count = 0
result = 0
while True:
    if result > S:
        count -= 1
        break
    else:
        result += num
        num += 1
        count += 1


print(count)
