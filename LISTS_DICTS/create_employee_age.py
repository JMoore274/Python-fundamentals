def create_employee_ages():
    return {
        "Alice": 30, "Ben": 25, "Sofia": 28
    }
    
# Tests
ages = create_employee_ages()
print(ages)            # {'Alice': 30, 'Ben': 25, 'Sofia': 28}
print(ages["Sofia"])   # 28
print(len(ages))       # 3