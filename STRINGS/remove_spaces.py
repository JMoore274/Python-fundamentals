def remove_spaces(text):
    return text.replace(" ", "")
# Test    
print(remove_spaces("fast break"))     # fastbreak
print(remove_spaces("  slam dunk  "))  # slamdunk
print(remove_spaces("nospaces"))       # nospaces