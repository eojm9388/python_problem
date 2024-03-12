T = int(input())

for tc in range(1, T+1):
    # Ai 와 Bj의 길이
    a, b = map(int, input().split())
    # Ai
    A = list(map(int, input().split()))
    # Bj
    B = list(map(int, input().split()))
    # 최댓값
    result = 0

    # 길이가 작은 리스트를 기준으로 순회해야한다.
    if a > b:
        # ex) a = 5, b = 3 이면, 3번 순회해야함
        for i in range(a-b+1):
            temp = 0
            # B는 전체순회, A는 일부분 순회
            for j in range(b):
                temp += A[i+j] * B[j]
            # 최댓값 갱신
            if temp > result:
                result = temp
    else:
        for i in range(b-a+1):
            temp = 0
            # A는 전체순회, B는 일부분 순회
            for j in range(a):
                temp += A[j] * B[i+j]
            # 최댓값 갱신
            if temp > result:
                result = temp
                
    print(f'#{tc}', result)

