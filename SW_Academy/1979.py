import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# 세로열에 밑 칸이 몇개 있는지 리스트로 반환해주는 함수
def column_check(x, y):
    # 한줄의 빈칸의 개수
    check_count = 0
    # 한 줄 당 빈칸의 수를 담을 리스트
    count_list = []
    # 범위를 벗어나기전까지
    while x < N:
        # 만약 해당 칸이 빈칸이라면 빈칸의 개수 1증가
        if word_map[x][y] == 1:
            check_count += 1
        # 빈칸이 아니라면 이때까지 더한 빈칸의 개수를
        # 리스트에 추가한 뒤 초기화
        else:
            count_list.append(check_count)
            check_count = 0
        # 밑으로 한칸
        x += 1
    # 반복문의 마지막에 빈칸을 찾게 될 경우를 위해
    # 리스트에 추가를 한번 더 한다.
    count_list.append(check_count)
    # 한줄 당 빈칸 개수 리스트 반환
    return count_list
# 가로열에 밑 칸이 몇개 있는지 리스트로 반환해주는 함수
# 세로열 함수와 같은 매커니즘
def row_check(x, y):
    check_count = 0

    count_list = []
    while y < N:

        if word_map[x][y] == 1:
            check_count += 1
        else:
            count_list.append(check_count)
            check_count = 0
        y += 1
    count_list.append(check_count)
    return count_list





for test_case in range(1, T + 1):
    # N: 퍼즐의 크기 K: 단어의 길이
    N, K = map(int, input().split())
    # 찾은 빈칸의 개수를 카운팅해 줄 리스트 생성
    counts = [0] * (N+1)

    # 퍼즐의 입력값 받아오기
    word_map = [list(map(int, input().split())) for i in range(N)]
    # 세로열의 빈칸 개수 리스트
    column_word_list = []
    # 가로열의 빈칸 개수 리스트
    row_word_list = []
    # 가로와 세로의 크기가 N이기 때문에 N줄 순회
    for i in range(N):
        # 가로와 세로 한줄의 빈칸 개수 리스트를 받아와 각 열의 빈칸 개수 리스트에 추가
        column_word_list.append(column_check(0, i))
        row_word_list.append(row_check(i, 0))
    # 각 열의 빈칸 개수 리스트가 이중 리스트이기 때문에
    # 중첩 반복문을 사용하여 빈칸의 길이에 해당하는 인덱스를
    # 넣어 찾은 빈칸 리스트 개수 카운팅 값 증가
    for row in row_word_list:
        for r in row:
            counts[r] += 1
    for column in column_word_list:
        for c in column:
            counts[c] += 1
    # 원하는 길이의 빈칸의 개수 출력
    print(f'#{test_case}', counts[K])
