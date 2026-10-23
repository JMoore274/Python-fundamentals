def find_biggest(numbers):
    biggest = numbers[0]
    for num in numbers:
        if num > biggest:
            biggest = num
    return biggest

# Tests
print(find_biggest([4, 17, 9, 2]))    # 17
print(find_biggest([-5, -1, -8]))     # -1
print(find_biggest([42]))             # 42