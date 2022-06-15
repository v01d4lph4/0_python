# 17. all unique

# check whether the given list has all unique elements.

# you can cast the list into a set() to eliminate duplicate 
# elements and compare the lengths. 
ex_list_0 = [1,2,2,3,4,5,5,6]
print(len(ex_list_0) == len(set(ex_list_0)))
#> False

ex_list_1 = ["a", "b", "c"]
print(len(ex_list_1) == len(set(ex_list_1)))
#> True

# 🎁 bonus: to check if a string has unique charcters, 
# a similar approach can be used by cast str to list.
name = "el0n_mu$k"
name_list = list(name)
#> ['e', 'l', '0', 'n', '_', 'm', 'u', '$', 'k']

print(len(name_list) == len(set(name_list)))
#> True
