T = int(input())

def cal_money(m, n):
    # 12월을 넘어가면 1년치 수영장 비용을 모두 계산
    if n >= 12:
        money_list.append(m)
        return
    
    # 1일권 구매
    cal_money(m+cost[0]*go_swimming[n], n+1)
    # 1달권 구매
    cal_money(m+cost[1], n+1)
    # 3달권 구매
    cal_money(m+cost[2], n+3)


# 완전탐색한다.

for test_case in range(1, T + 1):
    # 1일권, 1달권, 3달권, 1년권 이용료
    cost = list(map(int, input().split()))
    # 월별로 수영장에 가는 횟수
    go_swimming = list(map(int, input().split()))
    
    # 1년간 지불해야할 수영장 이용료를 모두 담은 리스트
    money_list = []
    # 모든 달에 1일권, 1달권, 3달권을 구매했을 때 발생하는 비용을 전부 구함
    cal_money(0, 0)
    # 1년권 추가
    money_list.append(cost[3])
    
    # 제일 적은 비용 출력
    print(f'#{test_case}', min(money_list))