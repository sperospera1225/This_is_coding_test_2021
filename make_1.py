x = int(input())
array = [0]*(x+1)

for i in range(1,x+1):
    a = i
    count = 0
    def inner(i,count):
        while i != 1:
            if array[i] != 0:
                count = count + array[i]
                break
            if i % 5 == 0:
                if array[i - 1] < array[i // 5]:
                    array[i] = array[i - 1] + 1
                    return None
                i = int(i//5)
            elif i % 3 == 0:
                if array[i - 1] < array[i // 3]:
                    array[i] = array[i - 1] + 1
                    return None
                i = int(i//3)
            elif i % 2 == 0:
                if array[i - 1] < array[i // 2]:
                    array[i] = array[i - 1] + 1
                    return None
                i = int(i//2)
            else:
                i -= 1
            count += 1
        return count
    result = inner(i,count)
    if result != None:
        array[a] = result

for i in array:
    print(i)

# x = int(input())
#
# d = [0] * (x+1)
#
# for i in range(2,x+1):
#     d[i] = d[i-1]+1
#
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i//2]+1)
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i//3]+1)
#     if i % 5 == 0:
#         d[i] = min(d[i], d[i//5]+1)
#
# for i in d:
#     print(i)