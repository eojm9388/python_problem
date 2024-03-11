#d(n)을 만드는 함수
def d_n(n):
    result = int(n)
    for i in n:
        result += int(i)

    return str(result)

# 만들어진 d(n)을 저장해둘 리스트
num = []

for j in range(1, 10001):
    num.append(d_n(str(j)))
    # d(n)을 만들어 저장해둔다

# num리스트에 없는 수들만 출력해준다
for k in range(1, 10001):
    if str(k) not in num:
        print(k)
