import sys
# 돌의 개수
N = int(input())
# 돌의 높이들
arr = list(map(int, input().split()))
# 최대 밟을 수 있는 돌의 수 리스트
cnt = [1] * N

for i in range(1, N):
    for j in range(i):
        # 이전 돌들을 보면서 자신보다 높이가 낮다면 제일 cnt가 많은 것중에 +1이다
        if arr[i] > arr[j]:
            cnt[i] = max(cnt[i], cnt[j]+1)

# 제일 많이 돌을 밟은 개수
print(max(cnt))