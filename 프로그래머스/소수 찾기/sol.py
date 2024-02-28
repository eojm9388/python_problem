# 소수를 찾는 함수
def prime_number(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    # 입력 받은 숫자의 개수
    N = len(numbers)
    # 입력 받은 숫자들로 순열 만들기
    def f(i, k):
        if i > k:
            return

        temp = num[:]
        num_list.append(temp)


        for j in range(N):
            if used[j] == 0:
                used[j] = 1
                num.append(numbers[j])
                f(i+1, k)
                used[j] = 0
                num.pop()
    # 사용한 숫자 처리용 -> f 함수에서 사용            
    used = [0] * N
    num = []
    num_list = []
    # f : numbers의 숫자들로 만들 수 있는 순열이 num_list에 저장되어있음
    f(0, N)
    # 소수의 개수 
    cnt = 0
    # num_list는 문자열로 이루어짐 -> 정수로 바꿀 num_list_int
    num_list_int = []
    # 정수로 바꿔서 저장한다
    while num_list:
        number = num_list.pop()
        # 빈 순열은 제외
        if number:
            # ['1', '2'] -> 12
            number = int(''.join(number))
            # 중복된 숫자는 제외하고 저장
            if number not in num_list_int:
                num_list_int.append(number)

    # print(num_list_int)
    # 소수의 개수 찾기
    while num_list_int:
        number = num_list_int.pop()
        if number > 1 and prime_number(number):
            cnt += 1

    
    
    return cnt