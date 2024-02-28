T = int(input())

# 모든 숫자들의 자리를 바꿔주는 함수 -> 조합 사용 -> [8(0), 4(1)] -> [4(1), 8(0)] -> 0과 1을 바꾸는 것과 1과 0을 바꾸는 것은 똑같다
# 자리가 바뀐 숫자들은 number_changed에 추가된다.
def f(i):
    # 숫자 2개를 선택해서 바꿔주기 때문에 N-1까지이다.
    # [1, 2, 3] 일때 i=3이라면 바꿔줄 숫자를 고를 수 없다
    if i == N-1:
        return
    # 바꿀 숫자는 인덱스가 고른 숫자보다 큰 것을 선택한다 -> 자기 자신을 두번 고를 순 없다
    for j in range(i+1, N):
        # 숫자 바꾸기
        temp[i], temp[j] = temp[j], temp[i]
        # 복사
        temp_2 = temp[:]
        # 이미 바꿔진 숫자에 들어있는 숫자라면 중복되니깐 스킵
        if temp_2 not in number_changed:
            # 바꿔진 숫자 리스트에 추가
            number_changed.append(temp_2)
        # 숫자 원 위치
        temp[i], temp[j] = temp[j], temp[i]
    # 다음 숫자 고르기
    # [1, 2, 3] i=0 인 1을 다 바꿔줬다면 다음인 i=1인 2를 고른다
    f(i+1)


# 문제풀이방법: 모든 숫자들의 자리를 바꾸고 리스트에 저장한다 -> 리스트에 저장된 숫자들을
#             다시 모두 자리를 바꾸고 저장한다 -> M번 한다 -> 그 중에 제일 큰 수를 구한다


for tc in range(1, T+1):
    # 숫자판 N, 바꿀 기회 M
    N, M = input().split()
    M = int(M)
    # 숫자판을 리스트로 바꾼다 123 -> ['1', '2', '3']
    number = list(N)
    # 숫자판의 숫자들의 크기를 구한다
    N = len(number)
    # 바꿔줄 숫자 리스트
    change_number = []
    # 처음에는 입력받은 숫자판을 바꿔줘야한다
    change_number.append(number)
    for n in range(M):
        # 바꿔준 숫자판을 입력받을 리스트
        number_changed = []
        # 모든 숫자판을 바꿔준다
        while change_number:
            # 바꿔줄 숫자판
            temp = change_number.pop()
            f(0)
        # number_changed 에는 바뀐 모든 숫자판이 있다
        # 복사해서 더해준다
        temp_changed = number_changed[:]
        change_number += temp_changed
        # 다음 숫자판을 바꿀때는 위에 저장된 change_number를 모두 다시 바꿔줘야한다

    # 지금 number_changed에는 M번 바꾼 숫자판들이 저장되어있다
    # 최댓값 찾기
    max_num = 0
    for new_num in number_changed:
        new_num = int(''.join(new_num))
        if max_num < new_num:
            max_num = new_num

    print(f'#{tc}', max_num)
