# 5. list comprehension

# ⚙️ syntax: [expression for item in iterable if condition == True]

[i for i in range(10) if i%2 == 0]
#> [0, 2, 4, 6, 8]

["Even" if num%2 == 0 else "Odd" for num in range(1,7)] 
#> ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']

[("Hello "+ name) for name in ['v01d','w0rld','4lph4']]
#> ['Hello v01d', 'Hello w0rld', 'Hello 4lph4']

# 🎁 bonus: one liner fizz-buzz
['FizzBuzz' if i%3==0 and i%5==0 else 'Fizz' if i%3==0 else 'Buzz' if i%5==0 else i  for i in range(1,20)]
#>  [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']


# 💡 protip: this can also be used to create sets
{x**2 for x in range(10) if x%2==0}
#> {0, 4, 16, 36, 64}
