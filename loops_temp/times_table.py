def times_table(num):
    result = []
    for i in range(1, 11):
        result.append(num * i)
    return result

# Tests
print(times_table(3))   # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
print(times_table(1))   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(times_table(0))   # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
