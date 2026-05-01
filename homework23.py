def check_value_frequency(test_dict, target_value):
    frequency = list(test_dict.values()).count(target_value)
    return frequency
test_dict = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 10}
value_to_check = 10
count = check_value_frequency(test_dict, value_to_check)
print(f"The frequency of value {value_to_check} is: {count}")