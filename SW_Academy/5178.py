# import sys
# sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 노드의 개수 N, 리프 노드의 개수 M, 출력할 노드 L
    N, M, L = map(int, input().split())
    # 완전 이진 트리
    tree = [0] * (N+1)
    
    # 리프 노드 입력
    for i in range(M):
        # 리프 노드의 번호 node, 리프 노드 내의 숫자 num
        node, num = map(int, input().split())
        tree[node] = num
    
    # 노드 내 숫자가 채워지지 않은 마지막 번호 
    last = N - M
    
    # 트리의 루트까지 숫자가 채워지도록 반복 
    while last:
        # 채워지지 않은 가장 나중의 부모 노드
        p = last
        # 그 부모 노드의 왼쪽 자식
        c_l = tree[p*2]
        # 오른쪽 자식이 있다면 추가
        if p*2+1 <= N:
            c_r = tree[p*2+1]
        # 아니면 0
        else:
            c_r = 0
        # 부모 노드는 자식 노드의 합
        tree[p] = c_l + c_r
        last -= 1
    # 원하는 노드 내의 숫자 출력
    print(f'#{tc}', tree[L])