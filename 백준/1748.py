N = int(input())
# 각 숫자가 가지는 자리수 
# ex) 1의 자리(1~9): 1, 10의 자리(10~99): 2 
num_cnt = 1
# 만들어진 수의 자리수
answer = 0
# 임시 변수
temp_num = 1

while N >= temp_num:
		# 현재 임시 변수에 10의 곱합 값이 N보다 작을 경우
		# N이 임시 변수보다 자리수가 높다
    if temp_num * 10 <= N:
		    # 따라서 한자리 높은 자리수까지 개수를 더해줌
		    # 이때 이전 자리수는 빼줘야함
        answer += (temp_num * 10 - temp_num) * num_cnt
        temp_num *= 10 
        num_cnt += 1
    else:
		    # 만약 자리수가 같은 상태라면 차이만큼만 더해주면 됨
        answer += (N - temp_num + 1) * num_cnt
        break

print(answer)
