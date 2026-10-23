def average_price(prices):
    total = 0
    count = 0
    for price in prices:
        total += price
        count += 1
    return total / count


# Tests
print(average_price([10, 20, 30]))     # 20.0
print(average_price([4.50, 5.50]))     # 5.0
print(average_price([100]))            # 100.0