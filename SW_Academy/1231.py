# import sys
# sys.stdin = open('input.txt')

# 중위순회
def in_order(now):
    if now != 0:
        # 왼쪽 자식부터
        in_order(tree[now][0])
        # 왼쪽 자식이 리턴 되면 해당 노드의 번호에 담겨져있는 알파벳 출력
        print(alphabet_list[now], end='')
        # 오른쪽 자식
        in_order(tree[now][1])


for tc in range(1, 11):
    # 노드의 수
    N = int(input())
    # 트리
    tree = [[0, 0] for _ in range(N+1)]
    # 노드의 번호에 해당하는 알파벳 정보를 저장할 리스트
    alphabet_list = [''] * (N+1)

    for i in range(N):
        # 정점 정보 입력
        line = list(input().split())
        # 해당 정점
        p = int(line[0])
        # 해당 정점의 알파벳
        alphabet = line[1]
        # 해당 정점을 인덱스로 하는 알파벳 리스트에 할당
        alphabet_list[p] = alphabet
        # 정점의 왼쪽, 오른쪽 자식
        c = list(map(int, line[2:]))
        # 왼쪽 자식만 있으면 0 1개 추가
        if len(c) == 1:
            c.append(0)
        # 자식이 없으면 0 2개 추가
        elif not c:
            c += [0, 0]
        # tree 연결
        tree[p] = c

    print(f'#{tc}', end= ' ')
    in_order(1)
    print()