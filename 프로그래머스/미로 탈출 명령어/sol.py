n, m, x, y, r, c, k = 3, 4, 2, 3, 3, 1, 5

answer = ''
d = abs(r - x) + abs(c - y)

if (k - d) % 2 == 1 or k < d:
    answer = 'impossible'

elif (k - d) >= 0:
    height = abs(r - x)
    width = abs(c - y)

    if r >= x:
        answer += 'd' * height

    if c <= y:
        answer += 'l' * width

    if c > y:
        answer += 'r' * width
    if r < x:
        answer += 'u' * height

    remain = (k - d)
    dot_x, dot_y = r, c

    while (abs(dot_x - r) + abs(dot_y - c)) < remain:
        if dot_x + 1 <= n:
            dot_x += 1
            answer += 'd'
            remain -= 1
            continue

        if dot_y - 1 >= 1:
            dot_y -= 1
            answer += 'l'
            remain -= 1
            continue

        dot_y += 1
        answer += 'r'
        remain -= 1

    if dot_y > c:
        answer += 'l' * abs(dot_y - c)
    else:
        answer += 'r' * abs(dot_y - c)
    answer += 'u' * abs(dot_x - r)


