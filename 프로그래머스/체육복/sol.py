def solution(n, lost, reserve):
    answer = 0
    # 학생들의 체육복 개수를 세기위한 리스트
    # 전부 가지고 있다
    clothes_counts = [0] + [1] * n + [0]
    # 도둑이 학생들의 체육복을 가져가서 체육복 감소
    for i in lost:
        clothes_counts[i] -= 1
    # 여벌의 체육복을 가져온 학생 체육복 추가
    for j in reserve:
        clothes_counts[j] += 1
    
    
    for k in range(1, n+1):
        # 1번부터 체육복이 없다면
        if clothes_counts[k] == 0:
            # 앞에 친구가 체육복이 2개라면 빌려오기
            if clothes_counts[k-1] == 2:
                clothes_counts[k-1] -= 1
                clothes_counts[k] += 1
            # 뒤에 친구가 체육복을 가지고 있다면 빌려오기
            elif clothes_counts[k+1] == 2:
                clothes_counts[k+1] -= 1
                clothes_counts[k] += 1
    # 체육복을 다 빌려주고 체육복을 가지고 있는 사람 수 구하기
    for student in clothes_counts:
        if student:
            answer += 1
    
    return answer