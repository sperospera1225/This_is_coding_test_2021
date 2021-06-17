n = int(input())
array = list(map(int,input().split()))
m = int(input())
array2 = list(map(int,input().split()))

for i in array2:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')