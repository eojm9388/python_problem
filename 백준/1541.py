arr = input()

# '-' 앞까지의 모든 숫자와 '+'를 묶어 괄호를 친다. 그러면 최솟값이 된다
num = []
temp = ''
# '-'로 구분해서 나눔 -> split('-')도 가능할 듯
for i in range(len(arr)):
    if arr[i] != '-':
        temp += arr[i]
    else:
        num.append(temp)
        temp = ''
num.append(temp)

# 처음 숫자는 +임으로 저장
result = sum(map(int, num[0].split('+')))
# 뒤에 수들은 '-'괄호안에 있는 수들이니까 빼준다
for n in num[1:]:
    A = sum(map(int, n.split('+')))
    result -= A

print(result)