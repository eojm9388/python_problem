import sys
sys.stdin = open('input.txt')

T = int(input())
# 0~9 까지 문자열로 나타낸 리스트
num_str_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]


for tc in range(1, T+1):
    # 테스트 케이스와 케이스 길이를 일시적으로 받아줄 리스트
    temp = list(input().split())
    # 테스트 케이스, 케이스 길이
    test_case, lenght = temp[0], int(temp[1])
    # 문자열 숫자 리스트를 정수형 숫자 리스트로 바꿔 담을 리스트
    num_int_list = []
    
    # 문자열 숫자
    str_list = list(input().split())
    # 문자열을 num_str_list에서 찾아 정수로 바꿔준다.
    for s in str_list:
        num_int_list.append(num_str_list.index(s))
    
    # 정수로 바꿔주었으니, 정렬 가능
    num_int_list.sort()
    # 테스트 케이스 출력
    print(test_case)
    # 정렬된 문자열 숫자 리스트를 순서대로 출력
    for i in num_int_list:
        print(num_str_list[i], end=' ')

    print()


