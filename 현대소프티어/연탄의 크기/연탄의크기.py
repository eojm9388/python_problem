N = int(input())
# 집들의 난로 반지름
arr = list(map(int, input().split()))
# 범위가 전부 100이하였기때문에 완전탐색
max_cnt = 0
for i in range(2, 100):
    cnt = 0
    # 연탄의 반지름의 배수인 난로의 개수 구하기
    for j in arr:
        if j % i == 0:
            cnt += 1

    max_cnt = max(max_cnt, cnt)

print(max_cnt)