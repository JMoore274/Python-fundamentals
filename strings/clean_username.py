def clean_username(username):
    return username.strip().lower()


# Tests
print(clean_username("  JMoore22  "))  # jmoore22
print(clean_username("ADMIN"))         # admin
print(clean_username("guest"))         # guest