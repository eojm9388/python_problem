def solution(citations):
    H_index = 1
    result = 0
    # H-index를 1부터 시작해서 비교하면서 증가시킨다.
    while H_index <= len(citations):
        # h번 이상 인용된 논문의 개수를 세기 위한 변수
        count_1 = 0
        # 논문들을 순회
        for citation in citations:
            # 논문의 인용횟수가 h번 이상일 경우
            if H_index <= citation:
                # 개수 증가
                count_1 += 1
        # h번 이상 인용된 논문의 개수가 h편 이상일 경우
        if count_1 >= H_index:
            # 최댓값 갱신
            if H_index > result:
                result = H_index
        # h 증가
        H_index += 1
                
    return result