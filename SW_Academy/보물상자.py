from collections import deque

T = int(input())

for tc in range(1, T + 1):
    # 숫자의 개수 N, K번째 큰수
    N, K = map(int, input().split())
    # 자물쇠 비밀번호
    numbers = list(input())
    # 한쪽 변에 있을 수 있는 숫자 개수
    one_side_cnt = N // 4
    # 생성 가능한 수를 담아둔 리스트
    side_num = []
    # 시계방향으로 하나씩 돌리기 때문에 queue로 생성
    q = deque()

    # 끝에 숫자부터 q에 넣어준다
    for _ in range(N):
        q.append(numbers.pop())

    # 한변에 들어갈 수 있는 숫자의 개수만큼 회전할 수 있음
    for _ in range(one_side_cnt):
        for i in range(0, N, one_side_cnt):
            # 큐를 리스트로 바꿔서 가져옴
            numbers = list(q)
            # 한변에 해당하는 숫자들을 받아온다
            one_side_num = numbers[i:i + one_side_cnt]
            # pop을 사용하였기 때문에 뒤집어서 붙여줘야함
            one_side_num.reverse()
            # 받아온 16진수를 10진수로 바꿔서 생성 가능한 수에 넣어준다
            one_side_num = int(''.join(one_side_num), 16)
            # 중복되지 않은 숫자들만 추가
            if one_side_num not in side_num:
                side_num.append(one_side_num)
        # 시계방향으로 한칸 회전하기
        temp = q.popleft()
        q.append(temp)

    # 생성 가능한 숫자들 내림차순 정렬
    side_num.sort(reverse=True)
    # print(side_num)
    # K번째로 큰 수 출력
    print(f'#{tc}', side_num[K - 1])

