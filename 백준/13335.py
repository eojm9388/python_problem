# 선입선출을 위한 큐
from collections import deque

N, W, L = map(int, input().split())

arr = list(map(int, input().split()))

# 남아있는 트럭
truck = deque(arr)
# 현재 다리에 있는 트럭, 초기에는 0으로 채워둠
path = deque([0] * W)
# 경과시간
time = 0

# 모든 트럭이 지나갈때까지
while truck:
    # 다리의 맨 앞의 트럭 통과
    path.popleft()
    # 만약 다음 트럭이 지나가도 최대하중을 넘지 않으면 트럭 추가
    if sum(path) + truck[0] <= L:
        path.append(truck.popleft())
    # 아니면 0 추가 (트럭이 더 못지나간다)
    else:
        path.append(0)

    time += 1

# 다리에 남아있는 트럭이 다 지나갈때까지
while path:
    path.pop()
    time += 1

print(time)