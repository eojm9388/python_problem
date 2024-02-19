# 빙고인지 확인하는 함수
def check():
    # 빙고 줄의 개수
    count = 0
    # 우하 대각선 True의 개수 -> 5개면 빙고 1줄
    count_1 = 0
    # 좌하 대각선 True의 개수 -> 5개면 빙고 1줄
    count_2 = 0
    for i in range(5):
        # 가로 한줄 빙고인지 확인
        if calls[i].count(True) == 5:
            count += 1
        # 세로 한줄 빙고인지 확인
        for j in range(5):
            if calls[j][i] == False:
                break
        else:
            count += 1
        # 우하 대각선
        if calls[i][i] == True:
            count_1 += 1
        # 좌하 대각선
        if calls[i][4-i] == True:
            count_2 += 1
    # 우하 대각선 한줄 빙고인지
    if count_1 == 5:
        count += 1
    # 좌하 대각선 한줄 빙고인지
    if count_2 == 5:
        count += 1
    # 빙고가 3줄 이상이라면 빙고
    if count >= 3:
        return True
    else:
        return False
       
# 사회자가 부른 번호를 체크하는 함수
def call(num):
    # 빙고판을 전체 순회하여 번호를 체크한다
    for i in range(5):
        for j in range(5):
            if binggo[i][j] == num:
                # 찾으면 체크하고 바로 리턴
                calls[i][j] = True
                return
# 빙고판 2차원 리스트
binggo = [list(map(int, input().split())) for _ in range(5)]
# 사회자가 부른 번호를 체크할 2차원 리스트 True:부름, False:안부름
calls = [[False]*5 for _ in range(5)]
# 사회자가 부른 번호 순서
numbers = []
# 번호 순서를 갱신해준다.
for i in range(5):
    nums = list(map(int, input().split()))
    numbers += nums

# 빙고가 되기 위해서는 최소 12번은 불러야한다.
# 12번째 번호까지는 그냥 체크
for i in range(5):
    for j in range(5):
        if binggo[i][j] in numbers[:12]:
            calls[i][j] = True
# 만약 12번째에 빙고라면 12 출력
if check():
    print(12)
# 아니면 한 번호씩 부르면서 빙고인지 체크
else:
    for k in range(12, 25):
        call(numbers[k])

        if check():
            print(k+1)
            break
        

# for n in range(5):
#     print(calls[n])

