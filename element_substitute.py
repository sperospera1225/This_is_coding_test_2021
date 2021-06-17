n, k  = map(int, input().split())
array1 = input().split()
array2 = input().split()

a=0
b=0
count = 0

while count < k:
    maximum = 0
    minimum = 10000001
    for i in range(len(array1)):
        if minimum >= int(array1[i]):
            minimum = int(array1[i])
            a = i

    for i in range(len(array2)):
        if maximum <= int(array2[i]):
            maximum = int(array2[i])
            b = array2.index(str(maximum)) # 이렇게도 쓸수있다.
    print(array1[a], array2[b])
    if array1[a] < array2[b]:
        array1[a], array2[b] = array2[b], array1[a]
    count += 1

sum = 0
for i in array1:
    sum += int(i)

print(sum)