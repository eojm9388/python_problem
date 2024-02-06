import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    K = int(input())
    # 글자판
    matrix = [list(input()) for _ in range(8)]
    # 회문의 개수
    result = 0
    # 글자판 전체 순회
    for i in range(8):
        # 행 방향 회문 검사
        for j in range(8-K+1):
            # 길이가 K인 글자 리스트
            str_row_1 = matrix[i][j:j+K]
            # 글자 리스트를 뒤집은 리스트
            str_row_2 = []
            # 글자 리스트 뒤집기
            for r_1 in range(K):     # (-1, -2, -3, ..., -K-1까지)
                str_row_2.append(str_row_1[-r_1-1])
            # 글자열이 회문이라면 개수 증가
            if str_row_1 == str_row_2:ㄴ
                result += 1
            # print(str_row_1)
            # print(str_row_2)
            # print()
        # 열 방향 회문 검사
        for k in range(8-K+1):
            # 글자 리스트
            str_column_1 = []
            # 글자 리스트를 뒤집은 리스트
            str_column_2 = []
            # i 고정, 글자 하나씩 추가
            for l in range(K):
                str_column_1.append(matrix[k+l][i])
            # 글자 리스트 뒤집기
            for r_2 in range(K):
                str_column_2.append(str_column_1[-r_2-1])
            # 글자열이 회문이라면 개수 증가
            if str_column_1 == str_column_2:
                result += 1
            # print(str_column_1)
            # print(str_column_2)
            # print()

    print(f'#{tc}', result)

