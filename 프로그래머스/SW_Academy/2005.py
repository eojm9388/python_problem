# import sys
# sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 1번째 줄은 항상 1이다
    # 위에 줄 리스트
    up = [1]
    # 테스트 케이스 출력
    print(f'#{tc}')
    # 1부터 N까지 반복
    for j in range(1, N+1):
        # 위에 줄을 이용하여 현재 줄 만들기
        # 현재 줄 리스트
        current = []
        # 현재 줄의 개수 만큼 반복
        for k in range(j):
            # 첫번째 순서라면
            if k-1 < 0:
                # 1을 추가
                current.append(1)
            # 마지막 순서라면 1을 추가
            elif k == j-1:
                current.append(1)
            # 아니라면 위에줄 한칸 앞 숫자와 위에 줄 자신 칸의 숫자를 더해서 추가한다
            else:
                current.append(up[k-1] + up[k])
        # 현재 줄 출력
        print(*current)
        # 위에 줄 갱신
        up = current


