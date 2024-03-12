def solution(brown, yellow):
    # 전체 면적
    area = brown + yellow
    # 노란색 격자의 세로 길이 -> 가정
    h = 1
    # 노란색 격자의 가로 길이 -> 가정
    w = yellow // h
    # 가로 길이와 세로 길이를 입력하면 전체 면적을 리턴하는 함수
    def f(width, height):
        inner = width * height
        outter = 2 * width + 2 * height + 4
        return inner + outter
    # 전체 면적과 현재 가로 세로 길이를 넣었을 때 구해지는 전체 면적이 같으면 그 가로 세로 길이가 
    # 노란색 격자의 실제 가로 세로 길이가 된다
    while area != f(w, h):
        # 가로 세로 길이 1씩 증가
        h += 1
        # 세로로 나누어지는 값이 아니라면 스킵
        if yellow % h != 0:
            continue
        w = yellow // h

    # 전체 사이즈는 노란색 격자 사이즈에 테두리를 더해야하기 때문에
    # 2씩 추가
    return [w+2, h+2]