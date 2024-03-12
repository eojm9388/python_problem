def solution(bandage, health, attacks):
    answer = 0
    # 최대 체력
    max_health = health
    # 마지막 공격의 턴 = 총 턴수
    final_attack = attacks[-1][0]
    # 공격의 하는 턴 번호 리스트
    attacks_turn = [attack[0] for attack in attacks]
    # 공격할 때 줄어드는 체력
    attacks_hp = [attack[1] for attack in attacks]
    # 현재까지 공격한 횟수
    attack_count = 0
    
    # 총 턴수, 번호를 1번부터 시작하여 0을 맨앞에 더미로 넣어줌
    turn = [health] * (final_attack+1)
    # 시전시간, 턴당 회복력, 추가 회복량
    bandage_time, turn_hp, plus_hp = bandage[0], bandage[1], bandage[2]
    
    # 턴을 진행한다.
    for t in range(1, len(turn)):
        # 공격을 당할 때
        if t == attacks_turn[attack_count]:
            # 체력이 깍인다
            health -= attacks_hp[attack_count]
            # 붕대의 시전시간이 초기화된다
            bandage_time = bandage[0]
            # 현재 공격 횟수 증가
            attack_count += 1
            # 만약 체력이 0이 됐다면
            if health <= 0:
                # 종료
                return -1
            # 아니라면 다음 턴으로 넘김
            else:
                continue
        # 만약 최대체력이 아니라면 = 공격을 당했었다
        if health < max_health:
            # 붕대 감기 시작
            # 시전 시간 감소
            bandage_time -= 1
            # 턴당 체력 회복
            health += turn_hp
            # 만약 시전 시간 모두 회복하였다면
            if bandage_time == 0:
                # 추가 체력회복
                health += plus_hp
                # 시전 시간 초기화
                bandage_time = bandage[0]
            # 만약 추가된 체력이 최대체력을 넘겼다면
            # 최대체력으로 유지
            if health > max_health:
                health = max_health
       
    return health