from collections import deque

N, K = map(int, input().split())

# 원을 큐로 만듬
q = deque(list(range(1, N+1)))

# 처음 출력
print('<', end='')

# 마지막 1개의 수만 남을 때까지 반복
while len(q) > 1:
    # K-1번 뒤로 옮기고 빼기 -> 원에서 K번째 사람 빼기
    for i in range(K-1):
        temp = q.popleft()
        q.append(temp)

    print(f'{q.popleft()}, ', end='')

# 마지막 출력
print(f'{q.popleft()}>')