def solution(numbers, target):
    answer = []
    N = len(numbers)
    bit = [0] * N
    # 배열을 만드는 함수
    def f(i, k, t):
        # 배열을 다 만들었을 경우
        if i == k:
            result = 0
            # 배열의 요소의 합을 구한다
            for j in range(k):
                result += bit[j]
            # 만약 배열의 합이 타켓 넘버라면 해당 배열을 결과리스트에 추가
            if result == t:
                # print(bit)
                answer.append(bit)
        # 배열이 덜 만들어짐        
        else:
            # 음수를 넣는다
            bit[i] = -numbers[i]
            f(i+1, k, t)
            # 돌아오면 양수를 넣는다
            bit[i] = numbers[i]
            f(i+1, k, t)
    
    # 재귀함수 실행
    f(0, N, target)
    
    return len(answer)