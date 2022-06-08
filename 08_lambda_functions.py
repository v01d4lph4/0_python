# 8. lambda - one liner functions

# A lambda function is a small anonymous function. 
# A lambda function can take any number of arguments, 
# but can only have one expression.

# ⚙️ syntax: func = lambda arguments : expression

sqr = lambda x: x * x 
sqr(10)                                       	#> 100

findmax = lambda x,y: x if x > y else y 
findmax(50, 90)                               	#> 90


# 🎁 bonus: one liner to generate prime numbers
list(filter(lambda x:all(x % y != 0 for y in range(2, x)), range(2, 20)))
#> [2, 3, 5, 7, 11, 13, 17, 19]
