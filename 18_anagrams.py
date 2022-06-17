# 18. anagrams

# check if two strings are anagrams💡
str_0 = "v01d"
str_1 = "01dv"
str_2 = "n0p3"

# method 1 - using sorted()
print(sorted(str_0) == sorted(str_1))               #> True
print(sorted(str_1) == sorted(str_2))               #> False

# method 2 - using collections.Counter()
from collections import Counter

print(Counter(str_0) == Counter(str_1))             #> True
print(Counter(str_0) == Counter(str_2))             #> False          

# ---

# 💡 an anagram is a word or phrase formed by rearranging the letters
# of a different word or phrase, typically using all the original
# letters exactly once.
