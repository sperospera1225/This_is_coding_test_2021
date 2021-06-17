n, m = map(int, input().split())
array = list(map(int, input().split()))
array = sorted(array, reverse=True)

def ricecake(array, target, start, end):
    if start > end:
        return start-1
    ssum = 0
    mid = (start + end) // 2

    for i in array:
        if i > mid:
            ssum += (i - mid)
    if ssum == target:
        return mid
    elif ssum > target:
        return ricecake(array, target, mid+1, end)
    else:
        return ricecake(array, target, start, mid-1)

result = ricecake(array, m, 0, array[0])
print(result)