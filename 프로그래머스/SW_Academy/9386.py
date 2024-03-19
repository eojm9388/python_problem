import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    # 0과 1로 구성된 수열
    num = input()
    # 최대 연속된 1의 개수
    max_count = 0
    # 현재까지 연속된 1의 개수
    count = 0

    # 수열 전체 순회
    for i in num:
        # 만약 현재 숫자가 0인데 전에 1이 있었더라면
        if i == '0' and count != 0:
            # 만약 지금까지 연속된 1의 개수가 제일 높다면 갱신신
            if max_count < count:
                max_count = count
            # 현재까지 연속된 1의 개수 초기화
            count = 0


        # 만약 현재 숫자가 1이라면 연속된 개수 증가
        if i == '1':
            count += 1
    # 수열의 마지막이 1로 끝나도 갱신
    if max_count < count:
        max_count = count

    print(f'#{test_case}', max_count)
