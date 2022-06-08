# 9. map

# map() function returns a map object(which is an iterator) of the results after applying 
# the given function to each item of a given iterable (list, tuple etc.)

# ⚙️ syntax: map(func, iter)
# func  : a function to which map passes each element of given iterable.
# iter  : a iterable which is to be mapped.

# example
def square(n):
  return n*n

nums = [i for i in range(5)]                                        #> [0, 1, 2, 3, 4]
sqaure_of_nums = map(square, nums)
list(sqaure_of_nums)                                                #> [0, 1, 4, 9, 16]

# 💡 protip: you can combine lambda with map to write one-liners, 
# for same example as above
nums = [i for i in range(5)]                                        #> [0, 1, 2, 3, 4]
sqaure_of_nums = map(lambda x: x**2, nums)                          #> [0, 1, 4, 9, 16]

# another example to join 2 lists
name = ["v01d", "el0n", "j3ff"]
surname = ["4lph4", "mu5k", "b3z0s"]
list(map(lambda fn,ln: "{} {}".format(fn, ln), name, surname))    	#> ['v01d 4lph4', 'el0n mu5k', 'j3ff b3z0s']
