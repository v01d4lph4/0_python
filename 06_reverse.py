# 6. reverse a string or list

# ⚙️ syntax: <object>[::-1]

# on strings
name = "v01d"
print(name[::-1])                         #> d10v

# on lists
series = [i for i in range(5)] 
print(series)                             #> [0,1,2,3,4]
print(series[::-1])                       #> [4,3,2,1,0]


# 🎁 bonus: check palindrome
words = ["racecar", "anakin", "civic"]
for word in words: 
  print(word == word[::-1])               #> True, False, True
