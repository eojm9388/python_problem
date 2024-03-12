# 중복 가능한 순열을 만들어주는 메서드
from itertools import product
# 입력값들
user = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500]

# 세일 퍼선트
sale = [40, 30, 20, 10]
# 이모티콘 개수
E = len(emoticons)
# 최대 판매액 result, 최대 이모티콘 플러스 구매자 수 buy_cnt
result = 0
buy_cnt = 0

# 할인이 가능한 모든 경우의 수 구하기
# 예) 이모티콘 개수 2 -> (40, 40), (40, 30), (40, 20) .... (10, 20), (10, 10)
sale_squence = list(product(sale, repeat=E))

# 모든 경우의 수에서 고객이 이모티콘을 사는지 구한다.
for sale_p in sale_squence:
    buy = 0
    money = 0
    
    # 고객 1명씩 이모티콘을 구매한다
    for u in user:
        cost = 0
        for i in range(E):
            # 만약 고객의 할인 비율보다 높다면 구매
            if sale_p[i] >= u[0]:
                cost += emoticons[i]*(100-sale_p[i])//100
                # 만약 가격 이상의 돈이라면 이모티콘 플러스 구매
                if cost >= u[1]:
                    cost = 0
                    buy += 1
                    break
        # 고객 1명이 이모티콘을 구매한 뒤 나온 금액
        money += cost
    # 위의 for문을 다 돌면 buy에 이모티콘 플러스를 구매한 사람의 수와
    # money에 이모티콘 구매 금액이 나온다
    
    # 만약 이모티콘 플러스의 개수가 이전보다 더 많다면 갱신
    if buy_cnt < buy:
        buy_cnt = buy
        result = money
    # 이모티콘 플러스의 개수는 같은데 구매 금액이 더 크다면 갱신
    elif buy_cnt == buy and result < money:
        result = money

print(buy_cnt, result)
print(sale_squence)