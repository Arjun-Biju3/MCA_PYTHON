# Create a list of first names
first_names = ["Alice", "Bob", "Charlie"]

# Initialize a variable to count the occurrences of 'a'
count_a = 0

# Loop through each name in the list
for name in first_names:
    # Count the occurrences of 'a' (both lowercase and uppercase) in each name
    count_a += name.lower().count('a')

# Display the total count of 'a' in the list
print("Total occurrences of 'a' in the list of first names:", count_a)
