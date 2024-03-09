user = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]

sale = [10, 20, 30, 40]

def DFS(n, money):
    if n == E:
        cost.append(money)
        return

    for i in range(4):
        if visited[n] == 0:
            visited[n] = 1
            if sale[i] >= u[0]:
                DFS(n+1, money+emoticons[n]*(100-sale[i])//100)
            else:
                DFS(n+1, money)
            visited[n] = 0


E = len(emoticons)
result = 0
cnt = 0

for u in user:
    cost = []
    visited = [0]*E
    DFS(0, 0)
    for c in cost:
        if c >= u[1]:
            cnt += 1
            break

    print(cost)


# print(cnt, result)
