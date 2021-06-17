money = int(input())
coin_types = [500,100,50,10]
coin_num = 0

for coin in coin_types:
    num = int(money)//coin
    money = money - (num*coin)
    coin_num += num

print(coin_num)