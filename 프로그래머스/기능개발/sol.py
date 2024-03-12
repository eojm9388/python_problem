from collections import deque
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

# 작업의 개수, 작업 속도를 큐에 넣어줌
q = deque(progresses)
s = deque(speeds)
result = []

# 큐가 빌때까지
while q:
    N = len(q)
    # 모든 작업을 각자의 작업 속도로 진행 시킴
    for i in range(N):
        q[i] += s[i]
    # 배포되는 작업 개수
    cnt = 0
    # 작업이 완료된 모든 작업 배포
    while q and q[0] >= 100:
        q.popleft()
        s.popleft()
        cnt += 1
    # 배포된 작업이 있다면 추가
    if cnt != 0:
        result.append(cnt)

print(result)
