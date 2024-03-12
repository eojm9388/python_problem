# import sys
# sys.stdin = open('input.txt')

from collections import deque

def cycle():
    # 1부터 5까지 암호의 맨 앞 숫자에 빼준다
    for i in range(1, 6):
        # 암호의 맨 앞 숫자
        num = q.popleft()
        # print(num)
        num -= i
        # 만약 숫자가 0이하라면 맨 뒤로 보내고 종료
        if num <= 0:
            num = 0
            q.append(num)
            return True
        # 뺀 숫자를 맨 뒤로 보내기
        else:
            q.append(num)

for t in range(1, 11):
    # 테스트 케이스 입력
    tc = int(input())
    # 처음 암호
    number = list(map(int, input().split()))
    # 암호변경이 8사이클을 돌면 전체 암호가 15씩 감소하고
    # 처음 순서로 돌아온다.
    # 따라서 15로 나눴을 때 최소 몫까지는 8사이클을 반복할 수 있다.
    number_share = []
    number_remainer = []
    # 최소 몫을 구하기 위한 반복문
    for i in range(1, 9):
        number_share.append(number[i-1] // 15)
        number_remainer.append(number[i-1] % 15)
    # ex) tc1
    # share: [636, 637, 636, 636, 637, 636, 636, 636]
    # remainer: [10, 1, 10, 13, 3, 11, 11, 11]
    # mini_share: 636
    mini_share = min(number_share)
    # print(number_share)
    # print(number_remainer)
    # print(mini_share)

    # 최소 몫보다 큰 수들은 큰만큼 나머지에 15를 곱해서 더해주면 된다.
    for i in range(1, 9):
        number_share[i-1] -= mini_share
        number_remainer[i-1] += 15 * number_share[i-1]
    # 8사이클씩 돌다가 더 이상 8사이클을 못 돌 경우
    # 남아있는 수
    # ex) [10, 16, 10, 13, 18, 11, 11, 11]
    # print(number_share)
    # print(number_remainer)
    # 만약 15로 나누었을 때 나머지가 0이 있다면
    # 15씩 더해줌 -> 안해주면 중간에 0이 있을 경우 답이 아님
    if number_remainer.count(0):
        for i in range(1, 9):
            number_remainer[i-1] += 15

    # 남은 수를 큐로 만들어 사이클을 돈다.
    q = deque(number_remainer)
    while True:
        if cycle():
            break

    print(f'#{tc}', end=' ')
    # 결과값 출력
    for j in q:
        print(j, end=' ')

    print()
