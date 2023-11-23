# Input string
input_string = input("Enter a string: ")

# Check if the string ends with 'ing'
if input_string.endswith("ing"):
    modified_string = input_string + "ly"
else:
    modified_string = input_string + "ing"

# Print the modified string
print("Modified string:", modified_string)
