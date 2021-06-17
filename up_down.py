n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

array2 = sorted(array,reverse=True)

for i in array2:
    print(i,end=' ')
