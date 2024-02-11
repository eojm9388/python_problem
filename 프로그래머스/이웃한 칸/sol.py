def solution(board, h, w):
    answer = 0
    # 보드판의 가로, 세로 길이
    n = len(board)
    # 같은 색깔의 개수
    count = 0
    
    dh = [0, 1, -1, 0] 
    dw = [1, 0, 0, -1]
    # 정해진 좌표의 색깔
    my_color = board[h][w]
    
    # 델타 탐색
    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]
        # 보드판안에 있을 때
        if 0<=nh<n and 0<=nw<n:
            # 정해진 좌표의 색깔이 인접한 색깔과 같은 경우 개수 추가
            if my_color == board[nh][nw]:
                count += 1

    return count