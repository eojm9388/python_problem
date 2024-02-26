# 아홉 난쟁이들의 키
smuff = [int(input()) for _ in range(9)]

# 아홉 난쟁이들 중 7명을 뽑아 부분 집합을 만든다.
for i in range(1<<9):
    # 부분 집합
    temp = []
    # 부분 집합의 개수 = 난쟁이의 수
    cnt = 0
    # 부분 집합의 합 = 키의 합
    total = 0
    for j in range(9):
        if i & (1<<j):
            temp.append(smuff[j])
            cnt += 1
            total += smuff[j]
    # 부분 집합의 개수가 7이고, 키의 총합이 100이면 일곱 난쟁이다
    if cnt == 7 and total == 100:
        result = temp
        break

result.sort()

for k in range(7):
    print(result[k])