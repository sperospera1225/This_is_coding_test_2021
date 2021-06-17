n = int(input())
count = 0
a=[3,13,23,30,31,32,33,34,35,36,37,38,39,43,53]

for i in range(0,n+1):
    if i in a:
        count += 60*60
        continue
    for j in range(0,60):
        if j in a:
            count += 60
            continue
        for k in range(0,60):
            if k in a:
                count += 1
                continue

print(count)