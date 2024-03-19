T = int(input())

for tc in range(1, T+1):
    # 당근의 수 N
    N = int(input())
    # 당근의 크기 리스트 C
    C = list(map(int, input().split()))
    # 연속으로 커지는 당근의 개수 리스트
    result = []
    # 현재 연속으로 커진 당근의 개수
    count = 1
    # 2번째 당근부터 순회
    for i in range(1, N):
        # 만약 앞에 있는 당근이 지금 당근보다 작다면 연속
        if C[i-1] < C[i]:
            count += 1
        # 앞에 있는 당근이 더 크거나 같다면 불연속
        else:
            # 개수 리스트에 추가하고 리셋
            result.append(count)
            count = 1

    result.append(count)
    # 최댓값 출력
    print(f'#{tc}', max(result))



