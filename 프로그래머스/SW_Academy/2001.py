import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# 해당 좌표에 파리채를 내려쳤을때 잡히는 파리의 수를 반환하는 함수
def spike(x, y):
    # 잡은 파리의 수
    result = 0
    # M 범위만큼 있는 파리의 수 더하기
    for i in range(M):
        for j in range(M):

            result += matrix[x+i][y+j]
    return result


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    spike_count = []
    matrix = [list(map(int, input().split())) for i in range(N)]
    # 0번부터 N-M번까지만 순회하면 전체좌표를 순회하기 때문에 아래와 같이 범위를 설정해준다.
    # ex) N=5, M=2 일때 0번부터 4번까지만 순회하면 된다. (가로 세로 각각)
    for i in range(N-M+1):
        for j in range(N-M+1):
            spike_count.append(spike(i, j))
    print(f'#{test_case}', max(spike_count))