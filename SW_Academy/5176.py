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
        in_order(now*2)
        after_tree[now] = num
        num += 1
        in_order(now*2+1)



for tc in range(1, T+1):
    # 노드의 개수
    N = int(input())
    # 노드에 들어갈 번호 -> 탐색 순서?
    num = 1
    # 완전 이진 트리
    before_tree = [0] + list(range(1, N+1))
    # 중위순회를 거친 완전 이진 트리
    after_tree = [0] * (N+1)
    # 중위순회
    in_order(1)
    # 1번 노드가 루트가 된다.
    print(f'#{tc}', after_tree[1], after_tree[(N//2)])
