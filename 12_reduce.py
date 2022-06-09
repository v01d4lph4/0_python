# 12. reduce

# reduce() performs functional computation called folding by taking a function and an iterable 
# (eg: list, tuple, dict etc.) as arguments and result is returned after applying the function 
# on the iterable cumulateively.

# ⚙️ syntax   : functools.reduce(func, iterable[, initializer])
# func        : two-argument function that will be applied to iterable to compute a final value.
# iterable    : can be built-in/user-defined iterable (like: list, string, dict)
# initializer : (optional) placed before the iterable during computation, default when the iterable is empty.
# returns a single value as output which is the result of whole iterable getting reduced cumulateively.

# an example to reduce a list of numbers to its sum
from functools import reduce 

nums = [1, 2, 3, 4]
ans = reduce(lambda x, y: x + y, nums)                            #> (((1+2)+3)+4)
print(ans)                                                        #> 10

# above example with initializer 
reduce(lambda x, y: x + y, nums, 10)                              #> ((((10+1)+2)+3)+4) ~ 20
reduce(lambda x, y: x + y, [], 10)                                #> 10

# 💡 protip: use reduce with in-built operator functions
from functools import reduce 
import operator

# using operator.add() to sum the list
nums = [-1, 5, 10, 6, 3]
reduce(operator.add, nums)                                        #> 23
 
# using operator.concat() to join strings
reduce(operator.concat, ["@", "v01d", "4lph4"])                   #> "@v01d4lph4"

