# Input a line of text
input_text = input("Enter a line of text: ")

# Split the input text into words
words = input_text.split()

# Initialize an empty dictionary to store word counts
word_counts = {}

# Iterate through the words and count their occurrences
for word in words:
    # Remove punctuation marks (such as '.', ',', etc.) from the word
    word = word.strip('.,!?"\'')
    
    # Convert the word to lowercase to ensure case-insensitive counting
    word = word.lower()
    
    # Increment the count for the word in the dictionary
    word_counts[word] = word_counts.get(word, 0) + 1

# Display the word counts
print("Word counts:")
print(word_counts)
