def solution(price, money, count):
    total = count * (price + price*count) / 2
    return total - money if total > money else 0


#more mathmatical solution
def solution(price, money, count):
    total = count * (price + price*count) / 2
    return abs(min(money - total, 0))