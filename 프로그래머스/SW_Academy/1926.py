# 정수 N
N = int(input())
# 출력값
result = ''
# 1부터 N까지 369안에 있는지 확인한다.
for i in range(1, N+1):
    # 문자열로 바꿔서 확인 -> 모든 자리를 확인하기 위해
    num = str(i)
    # 숫자에 369가 몇개 들어있는지
    count = 0
    # 369개수 구하기
    for j in num:
        if j in '369':
            count += 1
    # 숫자안에 369가 있다면
    if count > 0:
        # 개수만큼 - 추가
        result += '-'*count + ' '
    # 숫자안에 없다면
    else:
        # 숫자 그대로 추가
        result += num + ' '

print(result)

