def nonConstructibleChange(coins):
    change = 1
    coins.sort()
    print(coins)
    for i in range(len(coins)):
        if change < coins[i]:
            return change
        else:
            change += coins[i]

    return change


coins = [5, 7, 1, 1, 2, 3, 22]
res = nonConstructibleChange(coins)
print(res)
