N = int(input())

people = [list(map(int, input().split())) for _ in range(N)]

# 전부 1등으로 초기화
order = [1] * N


for i in range(N):
    for j in range(N):
        # 만약 자신보다 덩치 큰 사람이 있다면 개수 증가
        if i != j:
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                order[i] += 1

print(*order)