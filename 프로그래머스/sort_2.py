citations = list(map(int, input().split()))
answer = 1
result = 0
while answer <= len(citations):
    count_1 = 0
    count_2 = 0
    for citation in citations:
        if answer >= citation:
            count_1 += 1
        
    if count_1 >= answer:
        if answer > result:
            result = answer
    answer += 1
    print(result)