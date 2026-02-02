def some_function():
    x = 5
    print(x)

# print(x) # This will raise a NameError because x is not defined in this scope


x = 10
some_function()
print(x) # This will print 10 because x is defined in the global scope  
