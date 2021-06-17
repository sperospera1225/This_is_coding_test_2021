from collections import deque

n, m = map(int, input().split())
miro = list()
for i in range(n):
    miro.append(list(map(int,input())))

move = [[1,0],[0,1],[-1,0],[0,-1]]
x = 0
y = 0

queue = deque()
queue.append((x,y))

while queue:
    x, y = queue.popleft()
    for i in move:
        target_row = x + i[0]
        target_col = y + i[1]
        if 0 <= target_row < n and 0 <= target_col < m and miro[target_row][target_col] == 1:
            miro[target_row][target_col] = miro[x][y] + 1
            queue.append((target_row,target_col))

print(miro[n-1][m-1])
