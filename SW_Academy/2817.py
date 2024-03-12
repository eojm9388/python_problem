T = int(input())

for tc in range(1, T+1):
    # 자연수의 개수 N, 타켓 수 K
    N, K = map(int, input().split())
    # 자연수 수열
    number = list(map(int, input().split()))
    # 타겟 수를 만들 수 있는 경우의 수
    cnt = 0
    # 비트 연산을 사용한 부분집합 구하기
    for i in range(1, 1<<N):
        temp = 0

        for j in range(N):
            if i & (1<<j):
                temp += number[j]
                if temp > K:
                    break
        # 부분집합의 합이 K라면 경우의 수 추가
        if temp == K:
            cnt += 1
            # print(temp)
    print(f'#{tc}', cnt)