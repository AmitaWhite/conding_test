def lastedcoin(cost):

    numOfCoin=0

    last=cost

    coin500=last//500

    last=last-(coin500*500)

    coin100=last//100

    last=last-(coin100*100)

    coin50=last//50

    last=last-(coin50*50)

    coin10=last//10

    numOfCoin=coin500+coin100+coin50+coin10

    return numOfCoin


#in this function, we can make lasting coin as list data type
#for example

def lscoin(cost):
    #as travel list sequentialy, this algorithm gonna do greedy
    coin_list = [500, 100, 50, 10]
    count=0
    
    for coin in coin_list:
        count+=cost//coin
        cost%=coin

    return count

print(lastedcoin(1260))

print(lscoin(1260))
