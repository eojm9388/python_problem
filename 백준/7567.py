dishs = list(input())

before_dish = dishs[0]
result = 10
for dish in dishs[1:]:
    if dish == before_dish:
        result += 5

    else:
        before_dish = dish
        result += 10

print(result)