# 10. filter

# filter() method filters the given sequence with the help of a function that tests
# each element in the sequence to be true or not.

# ⚙️ syntax: filter(func, seq)
# func: function that tests if each element of a sequence true or not.
# seq: sequence which needs to be filtered, it can be sets, lists, tuples or any iterators.
# returns an iterator that is already filtered.

# example to filter out all Even numbers from sequence
seq = [i for i in range(1,11)]                                    #> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def isEven(num):                                                  
  return num % 2 == 0

list(filter(isEven, seq))                                         #> [0, 2, 4, 6, 8, 10]

# 💡 protip: filter can be combined with lambda for one-liners
# a quick example to check if the character is a vowel
seq = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
list(filter(lambda ch: ch in "aeiou", seq))                       #> ['a', 'e', 'i']


# 🎁 bonus: we can use filter with None as well
seq = [0, -1, "", "v01d", True, False, 1337, 0.0, {}, []]
list(filter(None, seq))                                           #> [-1, 'v01d', True, 1337]
