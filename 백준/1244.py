# 스위치 개수 N
N = int(input())
# 스위치 점등 상태
switch = [0] + list(map(int, input().split()))
# 학생 수 S
S = int(input())
# 학생 정보 리스트
student = [list(map(int, input().split())) for _ in range(S)]

# 학생 성별 s (1남자, 2여자), 학생이 받은 번호
for s, n in student:
    # 남학생일 경우
    if s % 2 == 1:
        # 받은 번호의 배수만 스위치 교체
        for i in range(n, N+1, n):
            if switch[i] == 1:
                switch[i] = 0
            else:
                switch[i] = 1
    # 여학생일 경우
    else:
        i = 1
        while True:
            # 좌우 대칭 스위치 번호
            l_n = n - i
            r_n = n + i
            # 범위에 없으면 반복문 탈출
            if l_n < 1 or r_n > N:
                break
            # 좌우가 대칭이면 교체
            if switch[l_n] == switch[r_n]:
                if switch[l_n] == 0:
                    switch[l_n] = switch[r_n] = 1
                else:
                    switch[l_n] = switch[r_n] = 0
                # 범위 1씩 증가
                i += 1
            # 좌우 대칭이 아니라면 반복문 탈출
            else:
                break
        # 본인 스위치 교체
        if switch[n] == 1:
            switch[n] = 0
        else:
            switch[n] = 1
# 20개 단위로 스위치 출력
for j in range(1, N, 20):
    print(' '.join(map(str, switch[j:j+20])))