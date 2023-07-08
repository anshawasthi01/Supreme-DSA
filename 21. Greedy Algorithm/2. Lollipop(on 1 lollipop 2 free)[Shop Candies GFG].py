
prices = [2, 8, 6, 9, 4, 7]
n = 6

# algo starts here
prices.sort()

amount = 0
buy = 0
free = n - 1

while buy <= free:
    amount += prices[buy]
    buy += 1
    free -= 1
    free -= 1

print("Answer is", amount)
