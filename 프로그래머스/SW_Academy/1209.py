import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    # 테스트 케이수 숫자
    N = int(input())
    # 100X100 배열 입력 받아오기
    number_matrix = [list(map(int, input().split())) for _ in range(100)]
    # 합의 최댓값
    max_total = 0
    
    for i in range(100):
        # 각 열의 합 구하기
        # j가 증가 (열 부분)
        total = 0
        for j in range(100):
            total += number_matrix[i][j]
        # 최댓값 갱신
        if total > max_total:
            max_total = total
        # 각 행의 합 구하기
        # k가 증가 (행 부분)
        total = 0
        for k in range(100):
            total += number_matrix[k][i]
        # 최댓값 갱신
        if total > max_total:
            max_total = total

        total = 0
        # 오른쪽 아래방향 대각선 합 구하기
        for l in range(100):
            # 행과 열의 번호가 같아야함
            if i == l:
                total += number_matrix[i][l]
        # 최댓값 갱신
        if total > max_total:
            max_total = total
        # 왼쪽 아래방향 대각선 합 구하기
        for m in range(100):
            # 행의 마지막 번호와 열의 시작 번호가 같아야함
            if (99-i) == m:
                total += number_matrix[99-i][m]
        # 최댓값 갱신
        if total > max_total:
            max_total = total

    print(f'#{N}', max_total)
