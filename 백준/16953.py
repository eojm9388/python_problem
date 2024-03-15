A, B = map(int, input().split())

# 연산 횟수
cnt = 1

# B가 A가 될때까지 연산한다
while A != B:
    # 만약 B의 일의 자리가 1이 아니고 홀수라면 2로 나눠줄 수 없기 때문에
    # A 만들기 불가
    if str(B)[-1] != '1' and B % 2 == 1:
        cnt = -1
        break
    else:
        cnt += 1
        # 일의 자리가 1이라면 1삭제
        if str(B)[-1] == '1':
            B //= 10
        # 아니라면 짝수니깐 나누기 2
        else:
            B //= 2
    # 만약 B가 A보다 작아지면 만들기 실패
    if A > B:
        cnt = -1
        break

print(cnt)