T = int(input())

def search(i, j):
    row = 0
    column = 0
    # 끝점 찾기
    # 자신은 0이 아니고 오른쪽과 아래쪽이 0이면 끝점
    while matrix[i+row][j] != 0:
        row += 1
    while matrix[i][j+column] != 0:
        column += 1

    return row, column



for tc in range(1, T+1):
    N = int(input())
    # 화학물질 용기 2차원 리스트 matrix
    # 화학 물질이 있는 곳의 시작점의 규칙은 자신의 화학물질 용기의 숫자는 0이 아니고,
    # 자신의 왼쪽과 위쪽의 화학물질 용기의 숫자가 0이다.
    # 끝점도 오른쪽과 아래쪽의 화학물질 용기의 숫자가 0이다.
    # 따라서 0, 0 에서도 이 규칙을 적용하기 위해 위쪽과 아래쪽에 0으로 채운 리스트를 만들고
    # 왼쪽 열과 오른쪽 열에 0을 하나씩 추가한다.
    matrix = [[0] * (N+2)]
    for _ in range(N):
        matrix.append([0] + list(map(int, input().split())) + [0])
    matrix.append([0] * (N+2))
    # 부분 행렬의 행과 열
    result = []

    for i in range(1, N+1):
        for j in range(1, N+1):
            # 시작점 찾기
            # 자신은 0이 아니고 왼쪽과 위쪽이 0이라면 시작점
            if matrix[i][j] != 0 and matrix[i-1][j] == 0 and matrix[i][j-1] == 0:
                result.append(list(search(i, j)))
    # 부분 행렬의 개수
    R = len(result)
    # 부분 행렬 정렬하기 - 버블 정렬 활용
    for n in range(R):
        for k in range(1, R-n):
            a, b = result[k]
            c, d = result[k-1]
            # 크기 비교
            if a * b < c * d:
                result[k-1], result[k] = result[k], result[k-1]
            # 크기가 같다면, 행 크기 비교
            elif a * b == c * d:
                if a < c:
                    result[k-1], result[k] = result[k], result[k-1]
    print(f'#{tc}', R, end=' ')
    # 정렬된 부분 행렬의 행과 열 출력
    for x, y in result:
        print(x, y, end=' ')

    print()
