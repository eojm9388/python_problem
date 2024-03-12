k = 80
dungeons = [[80,20],[50,40],[30,10]]
D = len(dungeons)
temp = []
visited = [0] * D
max_cnt = 0

# 완전탐색 - 순열
def f(i):
    global max_cnt
    # 이미 던전을 모두 돌았으면 더 돌 필요없다
    if max_cnt == D:
        return
    # 만약 순열을 만들었다면
    if i == D:
        # 갈 수 있는 던전을 구한다
        cnt = 0
        HP = k
        # print(temp)
        for hp, hp_minus in temp:
            if HP >= hp:
                HP -= hp_minus
                cnt += 1
        # 갈 수 있는 최대 던전 개수 갱신
        if max_cnt < cnt:
            max_cnt = cnt
        return

    # 순열 만들기
    for j in range(D):
        if visited[j] == 0:
            visited[j] = 1
            temp.append(dungeons[j])
            f(i+1)
            visited[j] = 0
            temp.pop()

f(0)
print(max_cnt)