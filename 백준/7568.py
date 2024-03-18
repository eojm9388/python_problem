N = int(input())

people = [list(map(int, input().split())) for _ in range(N)]

order = [1] * N

for i in range(N):
    for j in range(N):
        if i != j:
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                order[i] += 1

print(*order)