import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 1부터 12까지의 숫자 원소를 가진 리스트
    number = list(range(1, 13))
    # N: 부분집합의 개수, K: 부분집합의 합
    N, K = map(int, input().split())
    # 원하는 부분집합의 개수
    result = 0
    # 1부터 12까지 리스트의 부분집합을 모두 구한다.
    for i in range(1, 1<<12):
        temp = []
        for j in range(12):
            if i & (1<<j):
                temp.append(number[j])
        # 부분집합 중 개수와 합이 일치하면 결과값 증가
        if len(temp) == N and sum(temp) == K:
            result += 1


    print(f'#{test_case}', result)
