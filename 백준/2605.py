# 학생 수
N = int(input())
# 학생들이 뽑은 번호들
student = list(map(int, input().split()))
# 줄 선 번호
line = []
# 학생들을 잠시 보관해둘 스택
stack = []
for i in range(N):
    # 학생이 뽑은 번호만큼 스택에 저장
    for j in range(student[i]):
        stack.append(line.pop())
    # 헤당 학생 줄 세우기
    line.append(i+1)
    # 스택에 저장되어있는 학생들 다시 줄 세우기
    for j in range(student[i]):
        line.append(stack.pop())

print(*line)

