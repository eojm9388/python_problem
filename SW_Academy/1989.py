T = int(input())

for test_case in range(1, T + 1):
    word = input()
    word_list = list(word)
    word_list.reverse()
    word_reverse = ''.join(word_list)

    if word == word_reverse:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')

