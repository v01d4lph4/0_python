# 16. size of object

# in python, the usage of sys.getsizeof() can be done to find the storage 
# size of a particular object that occupies some space in the memory. 

# ⚙️ syntax : sys.getsizeof(obj)
# object    : object can be of any type - str, int, bool, list etc.   
# returns the size of the object in bytes.


import sys

ex_bool = True                            # 28 bytes                         
ex_int = 0                                # 28 byes on init 
ex_tuple = (0, 1)                         # 40 bytes on init + 8 bytes per item in list
ex_str = "v01d4lph4"                      # 49 bytes on init + 1 byte per char in str
ex_list = ["j3ff", "el0n", "b1ll"]        # 56 bytes on init + 8 bytes per item in list
ex_set = {True, False}                    # 0-4 - 216 bytes, 5-8  - 472 bytes and ...
ex_dict = {                               # 0-5 - 232 bytes, 6-10 - 360 bytes and ...
  "v01d": "4lph4",
  "j3ff": "b3z0s",
  "b1ll": "g4t3s",
  }


print(sys.getsizeof(ex_bool), "bytes")    #> 28 bytes
print(sys.getsizeof(ex_int), "bytes")     #> 24 bytes
print(sys.getsizeof(ex_tuple), "bytes")   #> 56 bytes
print(sys.getsizeof(ex_str), "bytes")     #> 58 bytes
print(sys.getsizeof(ex_list), "bytes")    #> 120 bytes
print(sys.getsizeof(ex_set), "bytes")     #> 216 bytes
print(sys.getsizeof(ex_dict), "bytes")    #> 232 bytes
