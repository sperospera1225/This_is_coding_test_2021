n = int(input())
array = list(map(int, input().split()))

result1 = 0
result2 = 0

d = [0]*(n+1)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[n-1])



# for i in range(len(array)):
#     if (i+1)%2 == 0:
#         result1 += array[i]
#     if (i+1)%2 != 0:
#         result2 += array[i]
#
# if result1>result2:
#     print(result1)
# else:
#     print(result2)