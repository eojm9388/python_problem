import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 스도쿠 맵
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    # 스도쿠 검증
    sudoku_True = True
    for i in range(9):
        # 만약 스도쿠 검증에 실패한다면 반복문 탈출
        if not sudoku_True:
            break
        # 행 방향 스도쿠 검증
        # 1~9까지의 숫자가 2개 이상이거나 0개면 스도쿠 검증 실패
        for num in range(1, 10):
            if sudoku[i].count(num) >= 2 or sudoku[i].count(num) == 0:
                sudoku_True = False
                break
        # 열 방향 스도쿠 검증
        # 숫자들을 카운팅 해줄 리스트 생성
        num_list = [0] * 9
        for j in range(9):
            # 스도쿠의 숫자들을 카운팅 리스트에 더해준다
            num_list[sudoku[j][i]-1] += 1
            # 만약 더한 숫자가 2개 이상일 경우 스도쿠 검증 실패
            if num_list[sudoku[j][i]-1] >= 2:
                sudoku_True = False
                break
        # 만약 카운트 리스트에 개수가 0개인 숫자가 있어도 스도쿠 검증 실패
        if num_list.count(0) >= 1:
            sudoku_True = False
            break

    if sudoku_True:
        # 3X3칸 스도쿠 검증
        for k in range(0, 9, 3):
            # 숫자들을 카운팅 해줄 리스트 생성
            num_list = [0] * 9
            # 열 방향 3곳 스도쿠 검사
            for x in range(3):
                for y in range(3):
                    num_list[sudoku[k+x][y]-1] += 1
            if num_list.count(0) >= 1:
                sudoku_True = False
            # 카운팅 리스트 초기화
            num_list = [0] * 9
            # 행 방향 3곳 스도쿠 검사
            for m in range(3):
                for n in range(3):
                    num_list[sudoku[m][k+n]-1] += 1
            # 만약 카운팅 리스트에 0이 한개라도 있다면 
            # 숫자가 없다는 것으로 스도쿠 검증 실패
            if num_list.count(0) >= 1:
                sudoku_True = False

    print(f'#{tc}', int(sudoku_True))
