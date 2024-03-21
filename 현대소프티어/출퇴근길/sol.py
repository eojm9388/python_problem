def DFS_go(i, k):
    if i == end:
        k = len(path)
        temp = path[1:k-1]
        go_path.append(temp)
        print(temp)
        return



    for j in adj[i]:
        if k != j:
            path.append(j)
            DFS_go(j, i)
            path.pop()

def DFS_back(i):
    if i == start:
        k = len(path)
        temp = path[1:k-1]
        back_path.append(temp)
        return

    for j in adj[i]:
        path.append(j)
        DFS_back(j)
        path.pop()

n, m = map(int, input().split())

adj = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)

start, end = map(int, input().split())
visited = [0] * (n+1)
visited[start] = 1
path = [start]
path_short = []
go_path = []
back_path = []
DFS_go(start, 0)
# visited = [0] * (n+1)
# visited[end] = 1
# path = [end]
# DFS_back(end)
# print(go_path)
# print(back_path)
# cnt = 0
# for i in go_path:
#     if i in back_path:
#         cnt += 1

# print(cnt)