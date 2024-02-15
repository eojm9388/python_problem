# import sys
# sys.stdin = open('input.txt')

from collections import deque

T = int(input())

for tc in range(1, T+1):
    # 화덕에 넣을 수 있는 피자 개수 N, 구울 피자 개수 M
    N, M = map(int, input().split())
    # 피자치즈양 리스트
    pizza_list = list(map(int, input().split()))
    # [대기번호, 피자치즈양] 을 담은 리스트
    wait_pizza_list = [[x, pizza_list[x]] for x in range(M)]
    # 화덕 - 큐
    fire = deque()
    # print(wait_pizza_list)
    # 처음 화덕에 N개 만큼 피자를 넣는다
    for i in range(N):
        fire.append(wait_pizza_list[i])
    # print(fire)
    # 다음 피자 순서 (인덱스)
    next_pizza_index = N

    # 화덕에 피자가 남아있을 때까지
    while fire:
        # 화덕에 피자가 한바퀴 돈다
        for j in range(N):
            # 1번자리 피자 꺼내기
            # 꺼낼 때 치즈양은 절반
            pizza = fire.popleft()
            pizza[1] //= 2
            # print(fire)
            # 만약 꺼낸 피자의 치즈양이 있을 때는 다시 화덕에 넣기
            # 이게 마지막에 꺼낸 피자가 된다
            if pizza[1]:
                fire.append(pizza)
            # 꺼낸 피자의 치즈양이 0이면
            else:
                # 남아있는 대기 피자가 있을 경우
                if next_pizza_index < M:
                    # 화덕에 피자 넣어주기
                    fire.append(wait_pizza_list[next_pizza_index])
                    # 피자 대기 번호 증가
                    next_pizza_index += 1
                # 남아있는 대기 피자가 없을 경우
                else:
                    # 화덕이 빌때 까지 굽기
                    if not fire:
                        break
                    continue
                # print(next_pizza_index)

    # 마지막에 꺼낸 피자의 인덱스 번호 출력
    print(f'#{tc}',pizza[0]+1)

