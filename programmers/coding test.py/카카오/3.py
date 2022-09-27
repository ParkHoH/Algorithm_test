from itertools import product

def solution(users, emoticons):
    n = len(emoticons)
    result = [0, 0]

    for discounts in product([40, 30, 20, 10], repeat=n):
        prices = []

        for i in range(n):
            prices.append(round(emoticons[i] * (100-discounts[i]) / 100))

        cnt_client = 0
        payed_cliend = 0

        for need_discount, limit_price in users:
            total_payed = 0
            stop = False

            for i in range(n):
                if discounts[i] >= need_discount:
                    total_payed += prices[i]

                    if total_payed >= limit_price:
                        cnt_client += 1
                        stop = True
                        break
            
            if not stop:
                payed_cliend += total_payed
        
        if cnt_client > result[0] or (cnt_client == result[0] and payed_cliend > result[1]):
            result = [cnt_client, payed_cliend]

    return result


# print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))