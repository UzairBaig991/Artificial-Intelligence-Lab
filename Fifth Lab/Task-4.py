my_str = input("Enter a sentence: ")
words = my_str.split()
words.sort()
print("The sorted words are:")
for word in words:
    print(word)