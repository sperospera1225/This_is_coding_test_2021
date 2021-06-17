n = int(input())
array = []

for i in range(n):
    a, b = map(str,input().split())
    array.append((a, int(b)))
    # record = input().split()
    # array.append((record[0], int(record[1])))

def scoresort(item):
    return item[1]

# array2 = sorted(array,key=scoresort)
array2 = sorted(array, key=lambda student: student[1])

for i in array2:
    print(i[0], end='')
# for i in array2:
#     print(i[0], end=' ')
