n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]
result = 0

a = m//(k+1)
b = m%(k+1)

first = first*k*a
second = second*a
third = b*first

print(first+second+third)