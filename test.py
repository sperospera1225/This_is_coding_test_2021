n, m = map(int,input().split())
a, b, d = map(int, input().split())
items = list()
for i in range(n):
    items.append(list(map(int, input().split())))

row = a
column = b
circle = [[0,-1],[-1,0],[0,1],[1,0]]
count = 0

while True:
    if row+circle[d][0] < 4 and column+circle[d][1] < 4 and items[row+circle[d][0]][column+circle[d][1]] == 1:
        row = row+circle[d][0]
        column = column+circle[d][1]
        if d == 0:
            d = 3
        else:
            d = d - 1
        items[row][column] = 2
        count += 1
    elif items[row+circle[d][0]][column+circle[d][1]] == 0 or 2:
        for i in circle:
            if d == 0:
                d = 3
            else:
                d = d - 1
            d1 = list()
            d1.append(d)
            if len(d1)%4 == 0:
                row = row+circle[(d+1)%4][0]
                column = column+circle[(d+1)%4][1]
                count += 1
    if items[row][column] == 0:
        break

print(count)
