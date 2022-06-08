# 7. swap two variables

a = 2
b = 4

# ❌ the old way
temp = a
a = b 
b = temp 
print(a,b)              		  #> 4, 2

# ✅ the python way
a, b = b, a
print(a,b)              		  #> 4, 2


# 💡 protip: 
# this can also be used to assign multiple variables in one go.
a, b, c = 10, "v01d", True
print(a,b,c)            		  #> 10, "v01d", True
