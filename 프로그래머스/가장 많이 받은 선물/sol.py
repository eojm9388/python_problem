def solution(friends, gifts):
    answer = 0
    # 친구들의 선물을 주고 받은 정보를 담은 딕셔너리
    friend_dict = {}
    # 친구들의 선물 지수를 담은 딕셔너리
    gift_index = {}
    # 친구들의 다음달 받을 선물 수를 담은 딕셔너리
    present = {}
    
    
    for friend in friends:
        # 각 딕셔너리 선언
        friend_dict[friend] = {}
        gift_index[friend] = 0
        present[friend] = 0
    # 친구들의 선물 정보를 담은 딕셔너리에 리스트로 주고 받은 선물 개수 선언
    for friend in friend_dict:
        for gift_list in friends:
            friend_dict[friend][gift_list] = [0, 0] # [준 선물, 받은 선물]
    
    for gift in gifts:
        # 선물기록의 첫번째는 준 사람, 두번째는 받은 사람
        name1, name2 = gift.split()
        # 선물을 준 친구의 준 선물 리스트 값 증가
        friend_dict[name1][name2][0] += 1
        # 선물을 받은 친구의 받은 선물 리스트 값 증가
        friend_dict[name2][name1][1] += 1
        # 선물 지수 계산
        gift_index[name1] += 1
        gift_index[name2] -= 1
     
    # 다음달에 받을 선물 계산
    for mine in friend_dict:
        for friend in friends:
            # 친구한테 준 선물이 받은 선물보다 많다면 자신이 선물을 받는다
            if friend_dict[mine][friend][0] > friend_dict[mine][friend][1]:
                present[mine] += 1
            # 같다면
            # 선물 지수를 비교해 높은 사람에게 선물을 준다.
            elif friend_dict[mine][friend][0] == friend_dict[mine][friend][1]:
                if gift_index[mine] > gift_index[friend]:
                    present[mine] += 1
    
    max_present = 0
    # 가장 많이 받은 선물의 수 구하기
    for my_present in present:
        if present[my_present] > max_present:
            max_present = present[my_present]
        
    
    return max_present