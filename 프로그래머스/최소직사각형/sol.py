def solution(sizes):
    # 지갑의 최소 크기
    answer = 0
    # 명함의 세로 길이
    height = []
    # 명함의 가로 길이
    width = []
    # 명함의 가로, 세로 중 큰 값을 가로에 넣고, 세로에 작은 값을 넣는다.
    # 그러면 지갑의 최소 크기는 최대 세로와 최대 가로를 곱하면 된다.
    for i, j in sizes:
        if i >= j:
            width.append(i)
            height.append(j)
        else:
            width.append(j)
            height.append(i)
    answer = max(width) * max(height)
    return answer