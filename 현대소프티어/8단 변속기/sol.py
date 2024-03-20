arr = list(map(int, input().split()))

# 초기 점검 상태를 mixed로 가정
check = 'mixed'

# 오름차순 검사를 했는데 for문을 모두 통과하면
# ascending
for i in range(8):
    if arr[i] != i+1:
        break
else:
    check = 'ascending'

# 내림차순 검사를 했는데 for문을 모두 통과하면
# descending
for j in range(8):
    if arr[j] != 8-j:
        break
else:
    check = 'descending'

print(check)