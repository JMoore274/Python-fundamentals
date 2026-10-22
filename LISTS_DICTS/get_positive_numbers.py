def get_positive_numbers(numbers):
    result = []
    for num in numbers:
        if num > 0:
            result.append(num)
    return result

# Tests
print(get_positive_numbers([3, -1, 0, 7, -5]))  # [3, 7]
print(get_positive_numbers([-2, -4]))           # []
print(get_positive_numbers([1, 2, 3]))          # [1, 2, 3] 