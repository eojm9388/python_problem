N = int(input())
arr = list(map(int, input().split()))

cnt = [1] * N
# DP 문제
# cnt[i] : arr[i]를 마지막 값으로 가지는 가장 긴 증가부분수열의 길이

for i in range(1, N):
    for j in range(i):
        # arr[i] > arr[j] 이면서 가장 큰 cnt[j]에 1을 더한 값이 cnt[i]가 된다
        if arr[i] > arr[j]:
            cnt[i] = max(cnt[i], cnt[j]+1)


print(max(cnt))