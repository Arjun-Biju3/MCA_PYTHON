# Input the first list of integers
list1 = input("Enter the first list of integers separated by spaces: ")
list1 = list1.split()  # Split the input string into a list of strings
list1 = [int(item) for item in list1]  # Convert the list of strings to a list of integers

# Input the second list of integers
list2 = input("Enter the second list of integers separated by spaces: ")
list2 = list2.split()  # Split the input string into a list of strings
list2 = [int(item) for item in list2]  # Convert the list of strings to a list of integers

# Check if the lists have the same length
if len(list1) == len(list2):
    print("Both lists have the same length.")
else:
    print("Both lists have different lengths.")

# Calculate the sum of each list
sum1 = sum(list1)
sum2 = sum(list2)

# Check if the lists sum to the same value
if sum1 == sum2:
    print("Both lists sum to the same value.")
else:
    print("Both lists do not sum to the same value.")

# Check if any value occurs in both lists
common_elements = set(list1) & set(list2)
if common_elements:
    print("Common elements in both lists:", common_elements)
else:
    print("There are no common elements in both lists.")
