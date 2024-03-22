# 이분 탐색
def binary_search(i):
    s, e = 0, n-1
    while s<=e:
        m = (s+e)//2
        # 만약 찾고자 하는 값을 찾았다면 그 인덱스를 반환
        if car[m] == i:
            return m
        # 찾고자 하는 값이 더 작으면 작은 부분 탐색
        elif car[m] > i:
            e = m - 1
        # 찾고자 하는 값이 더 크면 큰 부분 탐색
        elif car[m] < i:
            s = m + 1
    return -1

# 자동차 개수, 연비 중간값 개수
n, q = map(int, input().split())
# 자동차 연비 리스트
car = list(map(int, input().split()))
middle = []
# 중간값 리스트에 담아주기
for _ in range(q):
    middle.append(int(input()))
# 이분 탐색을 위해 car 리스트 정렬하기
car.sort()
# 중간값 이분 탐색
for i in middle:
    m = binary_search(i)
    # 만약 찾지 못했다면 중간값을 가질 수 없음
    if m == -1:
        print(0)
    # 찾았다면 만들 수 있는 경우의 수는
    # 중간값 = 연비가 작은 자동차 개수 * 연비가 큰 자동차 개수
    else:
        print((m) * (n-1-m))