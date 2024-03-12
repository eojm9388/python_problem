# import sys
# sys.stdin = open('input.txt')

T = int(input())
# 노드의 값이 저장되는 방식이
# 중위순회방식이다

def in_order(now):
    global num
    # now 값이 있다면
    # 중위순회
    if now != 0 and now <= N:
        # 왼쪽 자식 노드
        in_order(now*2)
        # 왼쪽 자식이 리턴되면
        # 현재 탐색 번호 할당
        tree[now] = num
        num += 1
        # 오른쪽 자식 노드
        in_order(now*2+1)



for tc in range(1, T+1):
    # 노드의 개수
    N = int(input())
    # 노드에 들어갈 번호 -> 탐색 순서?
    num = 1
    # 완전 이진 트리
    # 중위순회를 거친 완전 이진 트리
    tree = [0] * (N+1)
    # 중위순회
    in_order(1)
    # 1번 노드가 루트가 된다.
    print(f'#{tc}', tree[1], tree[(N//2)])
