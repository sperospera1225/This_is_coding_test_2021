n, m = map(int,input().split())
a, b, direction = map(int, input().split())
items = list()
for i in range(n):
    items.append(list(map(int, input().split())))

circle = [[0,-1],[-1,0],[0,1],[1,0]]
count = 1
turn_time = 0
items[a][b] = 2

while True:
    print(a,b,turn_time)
    target_row = a + circle[direction][0]
    target_column = b + circle[direction][1]
    if items[target_row][target_column] == 0:
        a = target_row
        b = target_column
        count += 1
        turn_time = 0
        direction -= 1
        if direction == -1:
            direction = 3
        items[target_row][target_column] = 2
        continue
    else:
        direction -= 1
        if direction == -1:
            direction = 3
        turn_time += 1

    if turn_time == 4:
        target_row = a + circle[(direction + 1) % 4][0]
        target_column = b + circle[(direction + 1) % 4][1]
        if items[target_row][target_column] == 2:
            a = target_row
            b = target_column
        elif items[target_row][target_column] == 1:
            break

print(count)


