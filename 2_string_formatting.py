# 2. string formatting

name, age, percent = "v01d4lph4", 0, 100.00 # multi type declaration

# 5 ways to format the following sentence using variables declared above ↓
# My name is v01d4lph4, and my age is 0. 100.0 percent!

# a. f-strings // Python 3+ only
print(f"My name is {name}, and my age is {age}. {percent} percent!")

# b. string.format() 
print("My name is {}, and my age is {}. {} percent!".format(name, age, percent))

# c. modulus operator
print("My name is %s, and my age is %d. %s perecent!" % (name, age, percent))

# d. concatenation
print("My name is "+name+", and my age is "+str(age)+ ". " + str(percent) + " percent!")

# e. string.join()
print(''.join(["My name is ", name, ", and my age is ", str(age), ". ", str(percent), " percent!"])
