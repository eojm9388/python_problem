# import sys
# sys.stdin = open('input.txt')

T = int(input())

# 붕어빵을 받을 수 있을지 검사하는 함수
def f(M, K):
    # 현재 시간 -> 붕어빵을 K개 만들고 다 팔면 갱신
    time = 0
    # 현재 판 붕어빵 개수 -> 붕어빵을 K개 만들고 다 팔면 갱신
    sell_count = 0
    while True:
        # 붕어빵을 판다
        for i in range(K):
            # sell_count+i = 붕어빵 대기번호
            # time + M -> K개 붕어빵을 만들기까지 시간
            # 자기의 대기번호때 붕어빵이 안만들어졌다면 불가능
            if person[sell_count+i] < time + M:
                print('Impossible')
                return
            # 대기번호의 손님이 모두 받아갔다면 성공
            elif sell_count+i == N-1:
                print('Possible')
                return
        # K개를 다 팔았으면 시간이랑 대기번호 갱신
        else:
            time += M
            sell_count += K



for tc in range(1, T+1):
    # 사람 수 N, M초 K개 붕어빵 생성
    N, M, K = map(int, input().split())
    # 손님들이 올 시간 리스트
    person = list(map(int, input().split()))
    # 시간들을 오름차순으로 정렬
    person.sort()
    print(f'#{tc}', end=' ')
    f(M, K)



