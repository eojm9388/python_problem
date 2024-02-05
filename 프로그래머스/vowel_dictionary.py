def solution(word):
    result = []
    # 알파벳 모음 완전탐색
    for i in ['A', 'E', 'I', 'O', 'U']:
        # 첫번째 단어 초기화
        words_1 = ''
        # 첫번째 단어 추가
        words_1 += i
        result.append(words_1)
        for j in ['A', 'E', 'I', 'O', 'U']:
            # 두번째 단어 초기화
            words_2 = ''
            # 두번째 단어 추가
            words_2 += words_1 + j
            result.append(words_2)
            for k in ['A', 'E', 'I', 'O', 'U']:
                # 세번째 단어 초기화
                words_3 = ''
                # 세번째 단어 추가
                words_3 += words_2 + k
                result.append(words_3)
                for l in ['A', 'E', 'I', 'O', 'U']:
                    # 네번째 단어 초기화
                    words_4 = ''
                    # 네번째 단어 추가
                    words_4 += words_3 + l
                    result.append(words_4)
                    for m in ['A', 'E', 'I', 'O', 'U']:
                        # 다섯번째 단어 초기화
                        words_5 = ''
                        # 다섯번째 단어 추가
                        words_5 += words_4 + m
                        result.append(words_5)
    # 단어 정렬                    
    # result.sort()
    return result.index(word) + 1