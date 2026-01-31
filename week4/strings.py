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

print(ord("A")) # Output: 65
print(chr(128640)) # Output: 🚀