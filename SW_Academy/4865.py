import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    # str2의 단어들과 개수를 담을 딕셔너리 생성
    word_dict = {w: 0 for w in str1}
    # 가장 많은 글자 개수
    max_count = 0

    for i in str2:
        # 만약 str1의 단어가 str2에 있을 때
        if word_dict.get(i) != None:
            # 그 단어의 개수 1 증가
            word_dict[i] += 1

    # 딕셔너리를 순회하면서 최대 개수 갱신
    for k in word_dict:
        count = word_dict[k]

        if max_count < count:
            max_count = count

    print(f'#{tc}', max_count)


