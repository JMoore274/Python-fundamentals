def count_vowels(text):
    count = 0
    for char in text:
        if char.lower() in "aeiou":
            count += 1
    return count


# Tests
print(count_vowels("Basketball"))  # 3
print(count_vowels("AEIOU"))       # 5
print(count_vowels("xyz"))         # 0