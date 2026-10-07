import string
sentence = input("Enter a sentence: ")
print("\nOriginal sentence:")
print(sentence)
no_punctuation = ""
for char in sentence:
    if char not in string.punctuation:
        no_punctuation += char
no_punctuation = no_punctuation.lower()
words = no_punctuation.split()
words.sort()
print("\nProcessed sentence:")
print(words)