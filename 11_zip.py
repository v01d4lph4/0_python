# 11. zip

# zip() takes iterables, aggregates them in a tuple, and returns it.

# ⚙️ syntax: zip(iterables) || zip(*iterables)
# can be built-in/user-defined iterables (like: list, string, dict)
# returns an iterator of tuples based on the iterable objects.

# example to zip together 2 lists
languages = ['pyth0n', 'g0lang', 'j4v4']
versions = [3.10, 1.18, 17]
list(zip(languages, versions))                  			#> [('pyth0n', 3.1), ('g0lang', 1.18), ('j4v4', 17)]

# 💡 protip: you can use zip to iterate over multiple lists in one loop
names = ["j3ff", "b1ll", "el0n"]
ages = [58, 66, 50]
companies = ["amaz0n", "micr0s0ft", "t3sla"]

for (name, age, company) in zip(names, ages, companies):
  print(name, ":", age, ":", company)						#> j3ff : 58 : amaz0n
															#> b1ll : 66 : micr0s0ft
															#> el0n : 50 : t3sla

# 🎁 bonus: we can use * operator to unzip a collection as well
coordinate = ['x', 'y', 'z']
value = [3, 4, 5]
resultList = list(zip(coordinate, value))					#> [('x', 3), ('y', 4), ('z', 5)]

c, v =  zip(*resultList)
print(c,v)													#> ('x', 'y', 'z') (3, 4, 5)
