preamble = 'We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America.'

# Example: Sort words alphabetically
words = preamble.split()
sorted_words = sorted(words)

# output sorted words
print("\nSorted Words: ")
for word in sorted_words:
    print(word, end = " ")
print()

# however we didn't change to original list:
print("\nOriginal Words: ")
for word in words:
    print(word, end = " ")
print()

# to sort the original list, we can use the sort() method
words.sort()
print("\nSorted Words (using sort()): ")
for word in words:
    print(word, end = " ")  
