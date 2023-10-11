# Input a string
input_string = input("Enter a string: ")

# Check if the input string is not empty
if len(input_string) >= 2:
    # Exchange the first and last characters
    new_string = input_string[-1] + input_string[1:-1] + input_string[0]
    
    # Display the new string
    print("String with first and last characters exchanged:", new_string)
else:
    print("Please enter a string with at least two characters.")
