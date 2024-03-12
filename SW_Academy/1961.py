import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # 행렬의 크기
    N = int(input())
    # 행렬을 입력받아 2차원 리스트로 선언
    matrix = [list(map(int, input().split())) for i in range(N)]
    
    print(f'#{test_case}')
    # 90도, 180도, 270도 3번 회전
    # 행렬의 길이 ex) 3
    for i in range(N):
        
        # 첫번째 줄 ex) 741 987 369    -> i=0, N=3
        rotation_line = ''
        # 90도 회전 ex) matrix[2][0] + matrix[1][0] + matrix[0][0] = 741
        for j in range(N-1, -1, -1):
            rotation_line += str(matrix[j][i])
        print(rotation_line, end=' ')
        rotation_line = ''
        # 180도 회전 ex) matrix[2][2] + matrix[2][1] + matrix[2][0] = 987
        for k in range(N-1, -1, -1):
            rotation_line += str(matrix[N-i-1][k])
        print(rotation_line, end=' ')
        rotation_line = ''
        # 270도 회전 ex) matrix[0][2] + matrix[1][2] + matrix[2][2] = 369
        for l in range(N):
            rotation_line += str(matrix[l][N-i-1])
        # 270도 회전 출력 후 다음줄로 넘어간다.
        print(rotation_line)
