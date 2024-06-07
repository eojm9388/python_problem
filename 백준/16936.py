N = int(input())

B = list(map(int, input().split()))
# 첫번째 수 찾기
def first_num():
    for i in B:
		    # 만약 2로 나눈 수가 B에 있을 경우, 첫번째 아님
        if i % 2 == 0 and i // 2 in B:
            continue
        # 만약 3을 곱한 수가 B에 있을 경우, 첫번째 아님
        elif i * 3 in B:
            continue
	      # 둘 다 없으면 첫번째 수
        else:
            return i

first_A = first_num()
print(first_A, end=' ')

# 첫번째 수부터 나3곱2를 수행하면서 수열 찾기 
def find_A(x):
    for i in B:
        if x * 2 == i or (x % 3 == 0 and x // 3 == i):
            print(i, end=' ')
            find_A(i)

find_A(first_A)

