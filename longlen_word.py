# Input list of words
words = input("Enter a list of words separated by spaces: ").split()

# Initialize a variable to keep track of the length of the longest word
longest_length = 0

# Iterate through the words to find the longest word
for word in words:
    word_length = len(word)
    if word_length > longest_length:
        longest_length = word_length

# Print the length of the longest word
print("Length of the longest word:", longest_length)
