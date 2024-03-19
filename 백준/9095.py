T = int(input())

def f(i):
    global cnt
    # 원하는 숫자를 넘어가면 리턴
    if i > N:
        return
    # 원하는 숫자를 만들 수 있으면 개수 증가
    if i == N:
        cnt += 1
        return
		# 1, 2, 3 중 하나를 골라 더해줌
    for j in range(1, 4):
        f(i+j)

for tc in range(T):
    N = int(input())
    cnt = 0
    f(0)

    print(cnt)