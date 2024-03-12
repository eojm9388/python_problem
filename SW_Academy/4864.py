import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # str에 list를 해주면 문자 하나씩 담은 리스트로 바뀐다
    matrix = [input() for _ in range(N)]

    # 회문인 문자열
    result = ''

    for i in range(N):
        # 길이가 M인 문자열
        str1 = ''
        # 가로방향 문자열 회문 비교
        for j in range(N-M+1):
            # 슬라이싱을 이용하여 M 길이의 문자열 구하기
            str1 = matrix[i][j:j+M]
            # 구한 문자열 뒤집기
            str2 = str1[::-1]
            # 비교해서 같으면 회문
            if str1 == str2:
                result = str1


        for k in range(N-M+1):
            # 세로방향 문자열 회문
            str1 = ''
            # 행을 순회하면서 각 자리의 문자 더하기
            for l in range(M):
                str1 += matrix[k+l][i]
            # 구한 문자열 뒤집기
            str2 = str1[::-1]
            # 비교해서 같으면 회문
            if str1 == str2:
                result = str1

    print(f'#{tc}', result)

    # print(matrix)