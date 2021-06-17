n = int(input())
move = list(map(str,input().split()))
x, y = 1,1

for one_move in move:
    if one_move == 'U':
        if x == 1:
            continue
        x -= 1
    elif one_move == 'D':
        if x == n:
            continue
        x += 1
    elif one_move == 'R':
        if y == n:
            continue
        y += 1
    elif one_move == 'L':
        if y == 1:
            continue
        y -= 1

print(x, y)
