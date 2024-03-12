# 앞바다에 존재하는 상어 수 N
# 먹을 수 있는 상어 수 K
# 현재 상어의 크기 T
N, K, T = map(int, input().split())

# 앞바다에 있는 상어의 크기
shark = list(map(int, input().split()))

# 내림차순 정렬 -> 큰거부터 앞에 있다
shark.sort(reverse=True)

# 먹을 수 있는 만큼 먹을 때까지 반복
while K > 0:
    # 만약 앞바다에 있는 모든 상어들이 현재 상어보다 작다면 다 먹을 수 있음
    if shark[0] < T:
        T += sum(shark[:K])
        break
    # 먹을 수 있는 상어 중 제일 큰 상어를 먹는게 이득
    for i in range(N):
        if shark[i] < T:
            T += shark[i]
            K -= 1
            N -= 1
            shark.pop(i)
            break
    # for else문 - 위에 for문에서 break가 걸리지 않았다면 먹을 수 있는 상어가 없는거임
    else:
        break

print(T)