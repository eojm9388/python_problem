# import sys
# sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 노드의 개수 N
    N = int(input())
    # 입력 받을 숫자들 num
    nums = list(map(int, input().split()))
    # 최소힙
    mini_hip = [0] * (N+1)
    # 마지막 노드의 조상 노드들의 합
    result = 0

    for i in range(1, N+1):
        # 입력받은 숫자들을 차례대로 마지막 노드에 넣어준다.
        mini_hip[i] = nums[i-1]
        # 입력 받은 번호의 노드 -> 현재 마지막 노드 -> 자식 노드
        c = i
        # 부모 노드
        p = i // 2
        # 부모 노드가 없을 때까지 반복
        while p:
            # 만약 자식 노드가 더 작다면 교환
            if mini_hip[c] < mini_hip[p]:
                mini_hip[c], mini_hip[p] = mini_hip[p], mini_hip[c]
                # 부모의 번호가 자식 번호의 노드가 된다.
                c = p
                # 다음 부모 노드의 번호로 이동
                p //= 2
            # 부모 노드가 더 작다면 노드 추가 완료
            else:
                break
    # 마지막 노드의 부모 노드의 번호
    n = N // 2
    while n:
        # 위로 올라가면서 조상 노드의 합을 구한다
        result += mini_hip[n]
        n //= 2


    print(f'#{tc}', result)