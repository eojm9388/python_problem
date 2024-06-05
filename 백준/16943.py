from itertools import permutations

A, B = map(int, input().split())
# 내림차순 정렬한 수의 순열 탐색
for num in permutations(sorted(str(A), reverse=True)):
    C = ''.join(num)
    # 첫번째까 0이면 패스
    if C[0] == '0':
        continue
    # 작은 순간 제일 큰 수
    if int(C) < B:
        print(C)
        break
# break가 안됐으면 못 만듬
else:
    print(-1)