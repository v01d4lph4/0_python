# 3. error handling

try:                        # lets you test a block of code for errors.
    a = int(input("Enter a:"))          
    b = int(input("Enter b:"))    
    print(a/b)

except ZeroDivisionError:   # lets you handle the error.
    print("Error! b can't be 0")

except ValueError:
    print("Error! Please input integers.")

else:                       # lets you execute code when there is no error.
    print("Success!")

finally:                    # lets you execute code, regardless of output of the try/except.
    print("End of division.")

