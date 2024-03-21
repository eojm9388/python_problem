T = int(input())

from collections import deque

for tc in range(T):
    # 수행할 함수들
    func = list(input())
    # 배열에 들어있는 수의 개수
    N = int(input())
    # 배열의 수들 -> [1,2,3] 이런 형식으로 들어오기 때문에 (,)으로 나눈뒤 앞 뒤에 []를 없애줌
    arr = list(input().split(','))
    arr[0] = arr[0].replace('[', '')
    arr[-1] = arr[-1].replace(']', '')

    # 수행할 함수의 각 개수를 구함
    cnt_R, cnt_D = func.count('R'), func.count('D')
    # 만약 버리기 함수가 수의 개수보다 많을 경우 에러
    if cnt_D > N:
        print('error')
    # 만약 빈 배열이 입력 됐다면 arr안에 ''가 있음 -> 따로 처리하는 이유
    elif arr == ['']:
        print('[]')

    else:
        arr = deque(arr)
        # 정방향
        direction = True
        # 수행할 함수 탐색
        for f in func:
            # 만약 뒤집기라면
            if f == 'R':
                # 정방향은 역방향
                if direction:
                    direction = False
                # 역방향은 정방향
                else:
                    direction = True

            # 버리기면 방향에 따라
            elif f == 'D':
                # 정방향이면 앞에서 버리기
                if direction:
                    arr.popleft()
                # 역방향이면 뒤에서 버리기
                else:
                    arr.pop()

        # 만약 빈 리스트라면 빈 리스트 출력
        if list(arr) == []:
            print('[]')
        
        else:
            arr = list(map(int, arr))
            # 방향이 역방향이면 리스트 뒤집기
            if direction == False:
                arr = arr[::-1]
            # 출력 형식에 맞게 출력
            print('[', end='')
            for i in range(len(arr)-1):
                print(arr[i], end=',')
            print(arr[-1],end=']')
            print()


