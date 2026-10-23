def count_high_scores(scores):
    count = 0
    for score in scores:
        if score >= 90:
            count += 1
    return count
        
# Tests
print(count_high_scores([95, 82, 90, 70, 100]))  # 3
print(count_high_scores([50, 60]))               # 0
print(count_high_scores([90, 90, 90]))           # 3