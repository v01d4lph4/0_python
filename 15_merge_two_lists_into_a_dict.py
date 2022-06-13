# 15. merge two lists into a dict

# Assume we have two lists in Python and we want to merge them in a dictionary
# form, where one list's items act as the dictionary's keys and the other's as
# values. This is a frequent problem often faced when writing code in Python.

keys_list = ['v01d', 'el0n', 'j3ff']
values_list = ['4lph4', 'mu$k', 'b3z0s']

# using the zip function with a loop
items_tuples = zip(keys_list, values_list) 
names_dict = {} 
for key, value in items_tuples: 
    if key not in names_dict: 
        names_dict[key] = value

print(names_dict)
#> {'v01d': '4lph4', 'el0n': 'mu$k', 'j3ff': 'b3z0s'}

# 💡 protip: you can skip the for loop by directly using dict()
names_dict = dict(zip(keys_list, values_list))
#> {'v01d': '4lph4', 'el0n': 'mu$k', 'j3ff': 'b3z0s'}

# 🎁 bonus: we can also use zip with dictionary comprehension
names_dict = {key:value for key, value in zip(keys_list, values_list)}
#> {'v01d': '4lph4', 'el0n': 'mu$k', 'j3ff': 'b3z0s'}
