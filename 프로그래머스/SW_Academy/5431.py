T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    # 과제를 제출한 학생 번호
    submit = list(map(int, input().split()))
    # 학생들의 번호 리스트
    student = [0] * (N+1)

    # 과제를 제출한 학생들의 번호를 체크
    for i in submit:
        student[i] = 1

    print(f'#{tc}', end=' ')
    # 과제를 제출하지 않은 학생의 번호가 나오면 출력
    for j in range(1, N+1):
        if student[j] == 0:
            print(j, end=' ')

    print()