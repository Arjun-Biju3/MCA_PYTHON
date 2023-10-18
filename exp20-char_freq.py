# Input string
input_string = input("Enter a string: ")

# Create an empty dictionary to store character frequencies
char_frequency = {}

# Iterate through the string to count character frequencies
for char in input_string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# Print character frequencies
for char, frequency in char_frequency.items():
    print(f"'{char}' occurs {frequency} time(s) in the string.")
