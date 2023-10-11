# Input a list of integers separated by spaces
input_str = input("Enter a list of integers separated by spaces: ")

# Split the input string into a list of strings
input_list = input_str.split()

# Initialize an empty list to store the modified values
result_list = []

# Loop through the input list and replace values greater than 100 with 'over'
for item in input_list:
    try:
        number = int(item)
        if number > 100:
            result_list.append('over')
        else:
            result_list.append(str(number))
    except ValueError:
        # Handle non-integer inputs gracefully
        result_list.append(item)

# Join the modified values into a string
result_str = ' '.join(result_list)

# Display the modified list
print("Modified list:", result_str)
