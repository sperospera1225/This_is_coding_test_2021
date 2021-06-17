loc = list(input())
item = ['a','b','c','d','e','f','g','h']

x = item.index(loc[0]) + 1
y = int(loc[1])
count = 0

pmov = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]

for mov in pmov:
    a = x + mov[0]
    b = y + mov[1]
    if a < 1 or b < 1 or a > 8 or b > 8:
        continue
    count += 1

print(count)
print(int(ord('a')))