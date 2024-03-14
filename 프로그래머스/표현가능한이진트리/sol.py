# 큐 사용
from collections import deque

def solution(numbers):
    answer = []
		# 중위순회
    def in_order(i):
        if i == 0:
            return
        
        in_order(tree[i][0]) 
        temp_str = temp.popleft()
        # print(temp_str, i)
        temp_2[i] = temp_str
        in_order(tree[i][1])
        
        
    for num in numbers:
        # 먼저 입력받은 수를 2진수로 만들어줘야함
        cnt = 1
        k = 0
        # 만들 수 있는지 체크
        check = True
        # 2진수로 만들기 -> 앞에 0이 더 붙을 수 있음
        num_bin = format(num, 'b')
        n = len(num_bin)
        # 포화이진트리의 개수는 항상 2**(high)-1
        while n > cnt:
            k += 1
            cnt += 2**k
        # 부족한 0의 개수를 앞에 붙여줌    
        num_bin = '0'*(cnt-n) + num_bin
        # 만들어준 2진수를 큐에 넣어줌 -> 중위순회에 사용하기 위해
        temp = deque(num_bin)
        
        
        # 중위순회 후 이진트리에 들어갈 숫자를 기록할 용도
        temp_2 = [0] * (cnt+1)
        # print(num_bin)
        # 중위순회를 하기 위한 2진 트리를 만들어줄거임
        tree = [[0, 0] for _ in range(cnt+1)]
        for i in range(1, cnt+1):
            # 왼쪽 자식과 오른쪽 자식이 있는 노드에 자식들 추가
            if i * 2 + 1 <= cnt:
                tree[i][0] = i*2
                tree[i][1] = i*2+1
        # 중위 순회
        in_order(1)
        # 포화이진트리의 노드 번호가 인덱스인 요소에 이진수의 값이 들어감
        #       1           이진수: 0111111 (63)
        #    2     3                      1    2    3    4    5    6    7                   
        #  4  5   6  7      temp_2 = [0, '1', '1', '1', '0', '1', '1', '1']
        
        # 부모 노드인 노드의 번호를 순회 
        # 예) 63 -> idx: 1, 2, 3
        for j in range(1, cnt-2**k+1):
            # 부모 노드가 0이라면
            if temp_2[j] == '0':
		            # 자식 노드들 중 1이 있다면 트리 생성 불가 
                if temp_2[tree[j][0]] == '1' or temp_2[tree[j][1]] == '1':
                    check = False
                
        # print(tree)
        # print(temp_2)
        if check:
            answer.append(1)
        else:
            answer.append(0)
            
        
        
    return answer