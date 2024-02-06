N, C, W = map(int, input().split())

# 나무의 길이를 저장할 리스트
tree = []
for i in range(N):
    tree.append(int(input()))

# 제일 긴 나무의 길이
long_tree = max(tree)
# 자를 나무의 길이 단위 ex) 길이가 1인 나무토막을 만든다
lenght = 1
# 결과값을 담을 리스트
result_list = []

# 나무 토막이 제일 긴 나무의 길이보다 클 수 없다
while lenght <= long_tree:
    # 결과값 초기화
    result = 0
    # 나무 리스트 순회
    for t in tree:
        # 자르는 횟수
        cut = 0
        # 만약 토막 길이와 나무의 길이가 같다면 자르지 않고 결과값에 추가
        if t == lenght:
            result += t * W
        # 나무의 길이가 토막보다 크다면 자르던가(자르는게 이득)
        # 안자르던가(안자르는게 이득)
        elif t > lenght:
            # t_1:잘랐을 때
            t_1 = t
            # 나무의 길이가 토막 단위로 깔끔하게 잘린다면
            if t % lenght == 0:
                cut += t // lenght - 1
            # 나무의 길이가 토막 단위로 잘리지 않는다면 1회 추가
            else:
                cut += t // lenght
            # 남은 잔나무는 빼준다
            t_1 -= t % lenght
            # 만약 자른 나무 토막을 파는것이 이득이라면
            if t_1 * W - cut * C > 0:
                # 결과값에 추가
                result += t_1 * W - cut * C
            # 손해라면 굳이 팔지 않는다
            else:
                pass
        # 토막보다 작은 나무는 팔 수 없다
        else:
            pass
    # 토막 단위 증가
    lenght += 1
    #결과값 리스트에 추가
    result_list.append(result)

# 최댓값 출력
print(max(result_list))


