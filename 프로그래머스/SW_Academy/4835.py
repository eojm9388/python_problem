T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split())) # 정수 리스트
    max_num_total = sum(arr[:M]) # 처음에는 제일 큰 수를 첫번째 이웃한 M개의 합으로 한다.
    min_num_total = sum(arr[:M]) # 처음에는 제일 작은 수를 첫번째 이웃한 M개의 합으로 한다.

    for i in range(1, N-M+1):
        # 2번째부터 이웃한 M개의 숫자의 합을 구한다.
        # M개씩 더해지기 때문에 N-M+1까지 반복한다
        # ex) N = 10, M = 3, index["7",8,9]가 최대이기 때문에 range(1, 8)이 되어야한다.

        num_total = sum(arr[i:i+M]) # i번부터 i+M번까지의 합
        if num_total > max_num_total: # 만약 최고합보다 크다면 최고합을 변경
            max_num_total = num_total
        elif num_total < min_num_total: # 만약 최저합보다 작다면 최저합 변경
            min_num_total = num_total

    print(f'#{test_case} {max_num_total-min_num_total}')