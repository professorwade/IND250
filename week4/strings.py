"""Week 4: Strings
Strings are sequences of characters.
You can use single quotes ' or double quotes " to create strings.
You can use triple quotes ''' or \""" for multi-line strings.

Note that triple quotes can also be used for multi-line comments.
triple quotes can also contain single and double quotes without needing to escape them.

Triple quotes are often used for docstrings, which are multi-line comments that describe functions, classes, or modules.

"""

a_string = "Hello my name is Wade."
print(len(a_string))

#b_string = a_string + len(a_string) # doesn't work
b_string = a_string + "   " + str(len(a_string))
print(b_string)

print(a_string[-5:-1]) # minus indices start at the end of the string

print('!' * 30) # repeats ! 30 times

# With 'r', it prints exactly as written
print(r"C:\users\new_folder")

sentence = "The quick brown fox"
print("fox" in sentence)    # Output: True
print("cat" in sentence)    # Output: False
sentence = sentence.upper()
print(sentence)             # Output: THE QUICK BROWN FOX

print(ord("A")) # Output: 65
print(chr(128640)) # Output: 🚀

# strings are made up of characters, which are represented by numbers in the computer
# consequently if I iterate over a string, I get each character one at a time
for char in "Hello":
    print(char)

# strings are compared lexicographically using the ASCII values of their characters    
print("A" < "B") # Output: True
print("apple" < "banana") # Output: True
print("apple" < "Apple") # Output: False, because lowercase letters have higher ASCII values than uppercase letters
print("apple" < "apples") # Output: True, because "apple" is shorter than "apples"


